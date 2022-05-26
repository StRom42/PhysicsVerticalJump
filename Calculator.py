from math import *
import numpy as np

class JumpCalculator ():
    def __init__(self, height, mass,):
        self.height = height
        self.mass = mass
        self.gravity_const = 9.81
        self.weight = self.mass * self.gravity_const
        self.push_off_distance = 0.4
        self.max_force = 3000
        self.max_velocity = 4
        self.decline_rate = 1.05
        self.peak_location = -self.push_off_distance * 0.15
        self.time_to_max_activation = 0.3
        self.center_height = int(self.height / 2) - self.push_off_distance
        
        
    def calc_jump_characteristics(self, duration, time_step):
        points_num = int(duration / time_step)
        
        data_trace = {
            "RFD": [],
            "RPD": [],
            "velocity": [],
            "height": [],
            "time": []
        }
        
        # Init variables
        current_time = 0
        next_time = 0

        current_distance = 0
        next_distance = 0

        current_velocity = 0
        next_velocity = 0

        current_acceleration = 0

        current_RFD = 0
        current_RPD = 0

        # Used to calculate RFD
        previous_GRF = 0

        # Used to calculate RPD
        previous_power = 0

        # List for saving kinetics trace
        # trace_data = vector("list", length = max_iter)
        trace_index = 1

        # --------------------------
        # summary data

        # Ground Reaction Force
        summary_peak_GRF = 0

        # Peak Velocity
        summary_peak_velocity = 0

        # Rate of Force Development
        summary_peak_RFD = 0

        # Peak Power
        summary_peak_power = 0


        # Rate of Power Development
        summary_peak_RPD = 0


        # ----------------------------------------
        # Simulation loop
        while next_distance <= self.push_off_distance:

            # Do the safety check
            if trace_index > points_num:
                print("Maximal iterations reached. Returning NULL. Check the simulation parameters")
                return

            # Update kinematic variables
            current_time = next_time
            current_distance = next_distance
            current_velocity = next_velocity

            # Get Force Generator output
            fgen_output = self.fgen_get_output(
                # Forward current state
                current_time = current_time,
                current_distance = current_distance,
                current_velocity = current_velocity)

            # Get kinetic output
            # These must be returned by `fgen_func`
            ground_reaction_force = fgen_output["ground_reaction_force"]
            propulsive_force = fgen_output["propulsive_force"]
            current_acceleration = fgen_output["acceleration"]

            # -------------------------------------------
            # Calculate the New state of the system using
            # Runge-Kutta 4 method
            dx1 = current_velocity
            dv1 = current_acceleration

            #---
            dx2 = current_velocity + (0.5 * time_step * dv1)
            dv2 = self.fgen_get_output(
                # Forward current state
                current_time = current_time + (0.5 * time_step),
                current_distance = current_distance + (0.5 * time_step * dx1),
                current_velocity = current_velocity + (0.5 * time_step * dv1))
            
            dv2 = dv2["acceleration"]

            # ---
            dx3 = current_velocity + (0.5 * time_step * dv2)
            dv3 = self.fgen_get_output(
                # Forward current state
                current_time = current_time + (0.5 * time_step),
                current_distance = current_distance + (0.5 * time_step * dx2),
                current_velocity = current_velocity + (0.5 * time_step * dv2))
            
            dv3 = dv3["acceleration"]

            # ---
            dx4 = current_velocity + (time_step * dv3)
            dv4 = self.fgen_get_output(
                # Forward current state
                current_time = current_time + (time_step),
                current_distance = current_distance + (0.5 * time_step * dx3),
                current_velocity = current_velocity + (0.5 * time_step * dv3))
            
            dv4 = dv4["acceleration"]

            dx = (dx1 + 2 * (dx2 + dx3) + dx4) / 6
            dv = (dv1 + 2 * (dv2 + dv3) + dv4) / 6

            # Update the new system state
            next_distance = current_distance + dx * time_step
            next_velocity = current_velocity + dv * time_step

            # --------------------------------------------
            # Summary metrics

            if current_velocity > summary_peak_velocity:
                summary_peak_velocity = current_velocity
            

            if ground_reaction_force > summary_peak_GRF:
                summary_peak_GRF = ground_reaction_force

            current_power = current_velocity * ground_reaction_force

            if current_power > summary_peak_power:
                summary_peak_power = current_power
            

            if trace_index > 1:
                current_RFD = (ground_reaction_force - previous_GRF) / time_step
                current_RFD /= 10
                
            if current_RFD < 0:
                current_RFD = 0

            if current_RFD > summary_peak_RFD:
                summary_peak_RFD = current_RFD

            current_RPD = (current_power - previous_power) / time_step
            current_RPD /= 10
            
            if current_RPD < 0:
                current_RPD = 0

            if current_RPD > summary_peak_RPD:
                summary_peak_RPD = current_RPD

            # --------------------------------------------
            # Save trace
            current_height = self.center_height - self.push_off_distance + current_distance
            data_trace["RFD"].append(current_RFD)
            data_trace["RPD"].append(current_RPD)
            data_trace["velocity"].append(current_velocity)
            data_trace["height"].append(current_height)
            data_trace["time"].append(current_time)

            # --------------------------------------------
            # Update the timer
            next_time = current_time + time_step

            # update trace index
            trace_index = trace_index + 1

            # Update previous_GRF
            previous_GRF = ground_reaction_force

            # Update previous_power
            previous_power = current_power
        # Main loop finished

        # --------------------------
        # Summary/Performance  metrics
        take_off_time = current_time
        take_off_velocity = current_velocity
        current_height = current_height
        
        while ceil(current_height) >= (self.center_height - self.push_off_distance):
            t = current_time - take_off_time
            current_velocity = take_off_velocity - self.gravity_const * t
            current_height = self.center_height + take_off_velocity * t - (self.gravity_const * t ** 2) / 2
            
            # --------------------------------------------
            # Save trace
            data_trace["RFD"].append(current_RFD)
            data_trace["RPD"].append(current_RPD)
            data_trace["velocity"].append(current_velocity)
            data_trace["height"].append(current_height)
            data_trace["time"].append(current_time)
            
            current_time += time_step
            
        time_in_air = current_time - take_off_time
            
        return data_trace, time_in_air
        
        
        
        
    
    def fgen_get_force_percentage(self, current_distance = 0,
                                      push_off_distance = 0.4,
                                      decline_rate = 1.05,
                                      peak_location = -0.06):
        if current_distance < 0:
            print("Current distance cannot be below zero.")
            return 0

        if push_off_distance < 0.3 or push_off_distance > 0.7:
            print("Push off distance needs to be within 0.3 - 0.7m.")
            return 0

        if peak_location > 0 or peak_location < -push_off_distance:
            print("Peak location needs to be lower than zero and larger than -Push off distance")
            return 0 

        if peak_location == 0 and decline_rate == 0:
            return 1

        peak_location = push_off_distance + peak_location

        y1 = sin((decline_rate * (peak_location - current_distance) + 1) * pi / 2)
        y2 = sin(((current_distance - peak_location) / (push_off_distance - peak_location)) * pi / 2 + pi / 2)

        force_percentage = y1 if current_distance < peak_location else y2
        force_percentage = 0 if current_distance > push_off_distance else force_percentage

        return force_percentage
                                      
    def fgen_get_activation(self, current_time,
                                initial_activation = 0,
                                time_to_max_activation = 0.3):
        if current_time < 0:
            print("Current time cannot be below zero.")

        if initial_activation < 0 or initial_activation > 1:
            print("Initial activation must be between 0 and 1.")

        if time_to_max_activation < 0:
            print("Time to maximal activation needs to be a positive number")

        IES = 1 / (time_to_max_activation)
        time_to_max_activation = time_to_max_activation * (1 - initial_activation)

        alpha = (4 * IES) / (1 - initial_activation) * 2.5

        activation = (1 - initial_activation) / (1 + exp(-alpha * (current_time - time_to_max_activation / 2))) + initial_activation


        if time_to_max_activation == 0:
            activation = [1]* len(activation)
        else:
            activation = 1 if time_to_max_activation == 0 else activation

        return activation

                                
    def fgen_get_viscous_force(self, current_velocity,
                                   max_force = 3000,
                                   max_velocity = 4):
        visc_factor = max_force / max_velocity
        return current_velocity * visc_factor
                                   
    def fgen_get_velocity(self, external_force, max_force = 3000, max_velocity = 4):
        return (max_force - external_force) / (max_force / max_velocity)
                                   
    def fgen_get_output(self, current_time = 0,
                            current_distance = 0,
                            current_velocity = 0):

        # Get percent of maximal force based on the current position (distance)
        push_off_perc = current_distance / self.push_off_distance

        force_percentage = self.fgen_get_force_percentage(
                                current_distance = current_distance,
                                push_off_distance = self.push_off_distance,
                                decline_rate = self.decline_rate,
                                peak_location = self.peak_location)

        # Maximal force that can be generate at particular position
        potential_force = self.max_force * force_percentage

        # -----------------------------
        # Get Force Generator activation

        # To calculate activation we need initial force percentage (t=0, d=0)
        # NOT the current force percentage
        force_percentage_init = self.fgen_get_force_percentage(
                                        current_distance = 0,
                                        push_off_distance = self.push_off_distance,
                                        decline_rate = self.decline_rate,
                                        peak_location = self.peak_location)
        
        potential_force_init = self.max_force * force_percentage_init

        initial_activation = self.weight / potential_force_init
        # ----------------------------

        activation = self.fgen_get_activation(
                        current_time = current_time,
                        initial_activation = initial_activation,
                        time_to_max_activation = self.time_to_max_activation)

        generated_force = activation * potential_force

        # Viscous force
        viscous_force = self.fgen_get_viscous_force(
                            current_velocity = current_velocity,
                            max_force = self.max_force,
                            max_velocity = self.max_velocity)

        # ----
        # We need to "scale" viscous force as we did max force using force percentage
        viscous_force = viscous_force * force_percentage

        # Total force, acting on the object
        ground_reaction_force = generated_force - viscous_force

        # ----
        # check if GRF is below zero (which is imposible)
        if ground_reaction_force < 0:
            ground_reaction_force = 0 if ground_reaction_force < 0 else ground_reaction_force
            print("GRF below zero. Please check your fucking model")

        # Propulsive or Net force acting to accelerate the object
        propulsive_force = ground_reaction_force - self.weight

        # Get acceleration
        acceleration = propulsive_force / self.mass

        # Get Power
        power = ground_reaction_force * current_velocity


        # Resulting kinetics
        kinetics = {
            "ground_reaction_force": ground_reaction_force,
            "propulsive_force": propulsive_force,
            "acceleration": acceleration,
            "power": power
        }
        return kinetics