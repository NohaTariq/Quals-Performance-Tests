import os
from locust import HttpUser, task, between
from dotenv import load_dotenv
import requests
import random



# Load environment variables from .env file
load_dotenv()


class CompanyUser(HttpUser):
    wait_time = between(1, 3)

    certifications = ["Certified Aboriginal Business (CAB)",
                      "Certified Business Enterprise (CBE)",
                      "Disadvantaged Business (DBE)",
                      "Emerging Business Enterprise (EBE)",
                      "Historically Under-Utilized Business (HUB)",
                      "Locally Based Business Enterprise (LBE)",
                      "Minority Business Enterprise (MBE)",
                      "Minority Business Enterprise (MBE) & Women's Business (WBE)",
                      "Service Disabled Veteran Owned Small Business (SDVOSB)",
                      "Small Business (SBE)",
                      "Veteran Business Enterprise (VBE)",
                      "Women's Business Enterprise (WBE)"
                     ]

    #Should probably choose 10 of these for performance
    trades = [
                 "access_control_hardware_devices",
                 "access_control_software_and_database_management",
                 "access_control_system_hardware",
                 "access_control_vehicle_identification_systems",
                 "acoustic_finishes",
                 "acoustic_insulation",
                 "acoustic_treatment",
                 "acoustical_ceiling_suspension_assemblies",
                 "acoustical_ceilings",
                 "administrative_requirements",
                 "aggregate_surfacing",
                 "air_barriers",
                 "air_outlets_and_inlets",
                 "airfield_construction",
                 "aluminum_decking",
                 "amusement_park_structures_and_equipment",
                 "anchor_tiebacks",
                 "applied_fireproofing",
                 "aquariums",
                 "architectural_concrete",
                 "architectural_wood_casework",
                 "architectural_woodwork",
                 "athletic_and_recreational_special_construction",
                 "athletic_and_recreational_surfacing",
                 "athletic_equipment",
                 "audio_video_systems",
                 "available_information",
                 "available_project_information",
                 "backing_boards_and_underlayments",
                 "base_courses",
                 "battery_equipment",
                 "bedroom_furnishings",
                 "bentonite_waterproofing",
                 "beverage_and_tobacco_manufacturing_equipment",
                 "bid_forms",
                 "biohazard_remediation",
                 "biological_decontamination",
                 "biological_treatment_systems",
                 "biopharmaceutical_manufacturing_equipment",
                 "bored_piles",
                 "bridges",
                 "broadcast_theater_and_stage_equipment",
                 "building_modules",
                 "built_up_bituminous_roofing",
                 "built_up_bituminous_waterproofing",
                 "bulk_material_conveying_equipment",
                 "cable_transportation",
                 "carpeting",
                 "cast_polymer_fabrications",
                 "cast_roof_decks",
                 "cast_stone_masonry",
                 "cast_underlayment",
                 "ceilings",
                 "cement_plastering",
                 "cementitious_grouting",
                 "centrifugal_fire_pumps",
                 "certificates_and_other_forms",
                 "chemical_manufacturing_equipment",
                 "clarification_and_modification_forms",
                 "classified_location_lighting",
                 "clean_agent_fire_extinguishing_systems",
                 "cleaning_and_waste_management",
                 "closeout_procedures",
                 "coastal_construction",
                 "cofferdams",
                 "coiling_doors_and_grilles",
                 "cold_formed_metal_framing",
                 "cold_formed_metal_joist_framing",
                 "cold_formed_metal_trusses",
                 "commissioning",
                 "commissioning_of_communications",
                 "commissioning_of_electrical_power_generation",
                 "commissioning_of_electrical_systems",
                 "commissioning_of_electronic_safety_and_security",
                 "commissioning_of_fire_suppression",
                 "commissioning_of_openings",
                 "commissioning_of_plumbing",
                 "commissioning_of_process_heating_cooling_and_drying_equipment",
                 "commissioning_of_special_construction",
                 "commissioning_of_specialties",
                 "commissioning_of_thermal_and_moisture_protection",
                 "commissioning_of_transportation",
                 "commissioning_of_utilities",
                 "common_work_results_for_communications",
                 "common_work_results_for_concrete",
                 "common_work_results_for_earthwork",
                 "common_work_results_for_electrical_power_generation",
                 "common_work_results_for_exterior_improvements",
                 "common_work_results_for_finishes",
                 "common_work_results_for_integrated_automation",
                 "common_work_results_for_masonry",
                 "common_work_results_for_metals",
                 "common_work_results_for_openings",
                 "common_work_results_for_plumbing",
                 "common_work_results_for_process_interconnections",
                 "common_work_results_for_transportation",
                 "common_work_results_for_utilities",
                 "communications_backbone_cabling",
                 "communications_equipment_room_fittings",
                 "communications_horizontal_cabling",
                 "communications_structures",
                 "communications_transmission_and_distribution",
                 "compartments_and_cubicles",
                 "composite_doors",
                 "composite_paneling",
                 "composite_reinforcing",
                 "composite_trim",
                 "composite_windows",
                 "computer_and_electronic_product_manufacturing_equipment",
                 "concrete_curing",
                 "concrete_finishing",
                 "concrete_form_masonry_units",
                 "concrete_forming",
                 "concrete_topping",
                 "conditions_of_the_contract",
                 "conservation_treatment_for_period_masonry",
                 "conservation_treatment_for_period_metals",
                 "conservation_treatment_of_period_finishes",
                 "constructed_wetlands",
                 "construction_aids",
                 "construction_facilities",
                 "construction_progress_documentation",
                 "contracting_forms_and_supplements",
                 "controlled_environment_rooms",
                 "conveyors",
                 "countertops",
                 "curbs_gutters_sidewalks_and_driveways",
                 "curtain_wall_and_glazed_assemblies",
                 "dam_construction_and_equipment",
                 "dampproofing",
                 "data_communications_hardware",
                 "data_communications_network_equipment",
                 "data_communications_peripheral_data_equipment",
                 "decorative_extruded_metal",
                 "decorative_metal_stairs",
                 "demolition",
                 "demonstration_and_training",
                 "detention_equipment",
                 "directories",
                 "display_cases",
                 "domestic_water_softeners",
                 "door_and_window_hardware",
                 "door_hardware",
                 "dredging",
                 "driven_piles",
                 "dry_placed_stone",
                 "dumbwaiters",
                 "earth_stripping_and_stockpiling",
                 "earthwork",
                 "elastomeric_membrane_roofing",
                 "electric_dumbwaiters",
                 "electric_traction_elevators",
                 "electrical",
                 "electrical_power_control_equipment",
                 "electronic_life_safety",
                 "electronic_security",
                 "elevators",
                 "emergency_response_systems",
                 "entrances",
                 "entrances_and_storefronts",
                 "epoxy_grouting",
                 "equipment",
                 "erosion_and_sedimentation_controls",
                 "escalators_and_moving_walks",
                 "evaporative_air_cooling_equipment",
                 "excavation_and_fill",
                 "existing_conditions_assessment",
                 "expansion_control",
                 "exterior_insulation_and_finish_systems",
                 "exterior_lighting",
                 "exterior_protection",
                 "exterior_stone_cladding",
                 "extra_high_voltage_ehv_switchgear_and_protection_devices",
                 "fabric_and_grid_reinforcing",
                 "fabric_structures",
                 "fabricated_engineered_structures",
                 "faced_panels",
                 "facility_fuel_piping",
                 "facility_lightning_protection",
                 "facility_maintenance",
                 "facility_maintenance_equipment",
                 "facility_operation",
                 "facility_performance_requirements",
                 "facility_potable_water_storage_tanks",
                 "facility_protection",
                 "facility_shell_performance_requirements",
                 "facility_storm_drainage",
                 "facility_water_distribution",
                 "fibrous_reinforcing",
                 "finish_carpentry",
                 "fire_protection_specialties",
                 "fire_pump_accessories",
                 "fire_suppression",
                 "fire_suppression_sprinkler_systems",
                 "fireplaces_and_stoves",
                 "firestopping",
                 "flags_and_banners",
                 "flooring",
                 "flooring_treatment",
                 "fluid_applied_flooring",
                 "fluid_applied_waterproofing",
                 "folding_doors_and_grilles",
                 "food_delivery_carts_and_conveyors",
                 "food_preparation_equipment",
                 "foodservice_storage_equipment",
                 "formed_metal_fabrications",
                 "fountains",
                 "fuel_cell_electrical_power_generation_equipment",
                 "furnishings",
                 "gas_detection_and_alarm",
                 "gas_phase_air_filtration",
                 "gas_process_equipment",
                 "gas_systems_for_laboratory_and_healthcare_facilities",
                 "gaseous_air_pollution_control_equipment",
                 "general_conditions",
                 "general_requirements",
                 "general_requirements_for_access_control_systems",
                 "geotechnical_instrumentation_and_monitoring_of_earthwork",
                 "geotechnical_investigations",
                 "glass_and_glazing",
                 "glass_fiber_reinforced_concrete",
                 "glass_glazing",
                 "glass_unit_masonry",
                 "glazed_canopies",
                 "glued_laminated_construction",
                 "grading",
                 "gypsum_plastering",
                 "healthcare_communications_and_monitoring_systems",
                 "heat_exchangers_for_hvac",
                 "heating_ventilating_and_air_conditioning_hvac",
                 "heavy_timber_construction",
                 "hospitality_equipment",
                 "hospitality_furniture",
                 "hvac_ducts_and_casings",
                 "hvac_insulation",
                 "hvac_water_treatment",
                 "hydraulic_elevators",
                 "hydrocarbon_storage",
                 "hydrocarbon_transmission_and_distribution",
                 "hydronic_piping_and_pumps",
                 "information_specialties",
                 "injection_grouting",
                 "instructions_for_procurement",
                 "instrumentation_and_control_for_electrical_power_generation",
                 "instrumentation_and_control_for_electrical_systems",
                 "instrumentation_and_control_for_fire_suppression_systems",
                 "instrumentation_and_control_for_hvac",
                 "integrated_automation",
                 "integrated_automation_control_and_monitoring_network",
                 "integrated_automation_control_of_conveying_equipment",
                 "integrated_automation_control_of_electronic_safety_and_security_systems",
                 "integrated_automation_control_sequences_for_communications_systems",
                 "integrated_automation_control_sequences_for_electrical_systems",
                 "integrated_automation_control_sequences_for_electronic_safety_and_security_systems",
                 "integrated_automation_instrumentation_and_terminal_devices_for_facility_equipment",
                 "integrated_automation_software",
                 "integrated_automation_systems_for_facility_equipment",
                 "integrated_automation_systems_for_network_equipment",
                 "integrated_construction",
                 "integrated_door_opening_assemblies",
                 "interior_lighting",
                 "interior_planters_and_artificial_plants",
                 "interior_public_space_furnishings",
                 "interior_shutters",
                 "interior_wall_paneling",
                 "interiors_performance_requirements",
                 "internal_combustion_engine_piping",
                 "intrusion_detection",
                 "irrigation",
                 "irrigation_components",
                 "irrigation_pumps",
                 "joint_protection",
                 "landscaping",
                 "lead_remediation",
                 "life_cycle_activities",
                 "lifts",
                 "liquid_process_equipment",
                 "louvered_equipment_enclosures",
                 "louvers",
                 "low_density_concrete",
                 "low_voltage_circuit_protective_devices",
                 "low_voltage_controllers",
                 "low_voltage_distribution_equipment",
                 "low_voltage_electrical_service_entrance",
                 "low_voltage_switchgear",
                 "low_voltage_transformers",
                 "maintenance_of_concrete",
                 "maintenance_of_earthwork",
                 "maintenance_of_existing_conditions",
                 "maintenance_of_masonry",
                 "maintenance_of_metals",
                 "maintenance_of_wood_plastics_and_composites",
                 "manufactured_brick_masonry",
                 "manufactured_fireplaces",
                 "manufactured_metal_casework",
                 "manufactured_plastic_casework",
                 "manufactured_site_specialties",
                 "manufactured_stone_masonry",
                 "manufactured_wood_casework",
                 "marine_construction_and_equipment",
                 "masonry",
                 "masonry_fireplaces",
                 "mass_concrete_for_dams",
                 "mass_notification",
                 "medium_voltage_circuit_protection_devices",
                 "medium_voltage_enclosed_bus_assemblies",
                 "medium_voltage_switchgear",
                 "medium_voltage_transformers",
                 "membrane_roofing",
                 "metal_castings",
                 "metal_doors_and_frames",
                 "metal_fabrications",
                 "metal_floor_plates",
                 "metal_framed_skylights",
                 "metal_frames",
                 "metal_railings",
                 "metal_specialties",
                 "metal_stair_treads_and_nosings",
                 "metal_stairs",
                 "metal_support_assemblies",
                 "mining_machinery_and_equipment",
                 "mirrors",
                 "miscellaneous",
                 "mixing_equipment",
                 "modified_bituminous_membrane_roofing",
                 "mortar_bed_tiling",
                 "multiple_contract_summary",
                 "multiple_trades",
                 "multiple_wythe_unit_masonry",
                 "murals",
                 "natural_roof_coverings",
                 "non_shrink_grouting",
                 "notice_of_award",
                 "odor_dispersing_and_masking_counteracting_equipment",
                 "office_accessories",
                 "office_furniture",
                 "office_shelters_and_booths",
                 "oil_and_gas_extraction_equipment",
                 "onsite_wastewater_disposal",
                 "operation_and_maintenance_for_electrical_power_generation",
                 "operation_and_maintenance_of_communications_systems",
                 "operation_and_maintenance_of_electrical_systems",
                 "operation_and_maintenance_of_electronic_safety_and_security",
                 "operation_and_maintenance_of_exterior_improvements",
                 "operation_and_maintenance_of_fire_suppression",
                 "operation_and_maintenance_of_hvac_systems",
                 "operation_and_maintenance_of_openings",
                 "operation_and_maintenance_of_plumbing",
                 "operation_and_maintenance_of_pollution_and_waste_control_equipment",
                 "operation_and_maintenance_of_process_gas_and_liquid_handling_purification_and_storage_equipment",
                 "operation_and_maintenance_of_process_heating_cooling_and_drying_equipment",
                 "operation_and_maintenance_of_specialties",
                 "operation_and_maintenance_of_transportation",
                 "operation_and_maintenance_of_utilities",
                 "other_conveying_equipment",
                 "other_facility_construction_performance_requirements",
                 "other_plastering",
                 "other_specialties",
                 "owner_furnished_products",
                 "packaged_compressor_and_condenser_units",
                 "packaged_generator_assemblies",
                 "packaged_water_and_wastewater_treatment_equipment",
                 "painting",
                 "painting_and_coatings",
                 "parking_control_equipment",
                 "partitions",
                 "patient_care_equipment",
                 "paving_and_surfacing",
                 "paving_specialties",
                 "payment_procedures",
                 "performance_requirements",
                 "pest_control_devices",
                 "petroleum_and_coal_products_manufacturing_equipment",
                 "pews_and_benches",
                 "photovoltaic_collectors",
                 "physical_decontamination",
                 "planting_accessories",
                 "planting_irrigation",
                 "planting_preparation",
                 "plants",
                 "plaster_and_gypsum_board",
                 "plaster_and_gypsum_board_assemblies",
                 "plaster_fabrications",
                 "plastic_composite_fabrications",
                 "plastic_doors",
                 "plastic_paneling",
                 "plastic_windows",
                 "play_field_equipment_and_structures",
                 "plumbing",
                 "plumbing_insulation",
                 "polychlorinate_biphenyl_remediation",
                 "positive_displacement_fire_pumps",
                 "post_tensioned_concrete",
                 "precast_architectural_concrete",
                 "precast_concrete_specialties",
                 "precast_structural_concrete",
                 "prefinished_paneling",
                 "pressure_resistant_doors",
                 "pressurized_tanks_and_vessels",
                 "price_and_payment_procedures",
                 "primary_control_valves",
                 "process_air_and_gas_filters",
                 "process_boilers",
                 "process_control_software",
                 "process_piping",
                 "procurement_and_contracting_requirements",
                 "procurement_forms_and_supplements",
                 "procurement_scopes",
                 "product_requirements",
                 "product_storage_and_handling_requirements",
                 "project_forms",
                 "project_identification",
                 "project_utility_sources",
                 "quality_assurance",
                 "quality_control",
                 "quality_requirements",
                 "rail_tracks",
                 "railway_construction",
                 "recreational_equipment",
                 "refrigerant_detection_and_alarm",
                 "refrigerant_piping",
                 "reinforcement",
                 "reinforcement_bars",
                 "removal_and_disposal_of_contaminated_soils",
                 "removal_and_salvage_of_construction_materials",
                 "residential_plumbing_fixtures",
                 "resilient_flooring",
                 "retail_and_service_equipment",
                 "retaining_walls",
                 "rigid_paving",
                 "riprap",
                 "roadway_construction",
                 "roadway_signaling_and_control_equipment",
                 "roll_roofing",
                 "roof_and_deck_insulation",
                 "roof_panels",
                 "roof_pavers",
                 "roof_specialties",
                 "roof_tiles",
                 "roof_windows",
                 "roof_windows_and_skylights",
                 "roofing",
                 "rough_carpentry",
                 "safety_lighting",
                 "safety_specialties",
                 "sanitary_sewerage_equipment",
                 "sanitary_sewerage_piping",
                 "scaffolding",
                 "schedules_for_earthwork",
                 "schedules_for_electrical",
                 "schedules_for_electrical_power_generation",
                 "schedules_for_finishes",
                 "schedules_for_hvac",
                 "schedules_for_masonry",
                 "schedules_for_metals",
                 "schedules_for_openings",
                 "schedules_for_plumbing",
                 "schedules_for_thermal_and_moisture_protection",
                 "schedules_for_transportation",
                 "schedules_for_wood_plastics_and_composites",
                 "seating",
                 "security_control_equipment",
                 "security_equipment",
                 "security_monitoring_and_control",
                 "selective_clearing",
                 "selective_tree_and_shrub_removal_and_trimming",
                 "service_walls",
                 "sheathing",
                 "sheet_metal_flashing_and_trim",
                 "sheet_metal_roofing",
                 "sheet_metal_roofing_specialties",
                 "sheet_metal_wall_cladding",
                 "sheet_metal_waterproofing",
                 "shingles_and_shakes",
                 "signage",
                 "single_wythe_unit_masonry",
                 "site_cast_concrete",
                 "site_construction_performance_requirements",
                 "site_containment",
                 "site_furnishings",
                 "site_grounding",
                 "site_improvements",
                 "site_remediation",
                 "sliding_glass_doors",
                 "slope_protection",
                 "slotted_channel_framing",
                 "slurry_walls",
                 "snow_control",
                 "soil_reinforcement",
                 "soil_stabilization",
                 "soil_treatment",
                 "solar_energy_electrical_power_generation_equipment",
                 "solar_energy_heating_equipment",
                 "solicitation",
                 "special_coatings",
                 "special_facility_components",
                 "special_foundations",
                 "special_function_doors",
                 "special_function_glazing",
                 "special_instrumentation",
                 "special_purpose_lighting",
                 "special_wall_surfacing",
                 "specialized_liquid_pumps",
                 "specialty_casework",
                 "specialty_doors_and_frames",
                 "specialty_element_construction",
                 "specialty_flooring",
                 "specialty_placed_concrete",
                 "staining_and_transparent_finishing",
                 "steam_and_condensate_piping_and_pumps",
                 "steel_decking",
                 "steel_joist_framing",
                 "stone_facing",
                 "stone_masonry",
                 "storage_specialties",
                 "storage_tanks_for_fire_suppression_water",
                 "storefronts",
                 "stormwater_conveyance",
                 "stormwater_utility_equipment",
                 "stressed_tendon_reinforcing",
                 "structural_aluminum_framing",
                 "structural_composite_shapes_and_plates",
                 "structural_concrete",
                 "structural_rod_assemblies",
                 "structural_steel_framing",
                 "structure_and_building_moving_relocation",
                 "structure_moving",
                 "subdrainage",
                 "substation_converter_stations",
                 "substations",
                 "summary_of_work",
                 "supports_for_plaster_and_gypsum_board",
                 "surface_water_sources",
                 "surge_protective_devices",
                 "surveys",
                 "swimming_pools",
                 "switchboards_and_panelboards",
                 "systems_furniture",
                 "telephone_specialties",
                 "temporary_barriers_and_enclosures",
                 "temporary_construction",
                 "temporary_facilities_and_controls",
                 "tension_rod_and_cable_truss_assemblies",
                 "terrazzo_flooring",
                 "textured_ceilings",
                 "thermal_insulation",
                 "thermal_storage",
                 "thermoplastic_membrane_roofing",
                 "thin_set_tiling",
                 "toilet_bath_and_laundry_accessories",
                 "towers",
                 "traffic_coatings",
                 "traffic_doors",
                 "transfer_switches",
                 "translucent_wall_and_roof_assemblies",
                 "transplanting",
                 "transportation_and_disposal_of_hazardous_materials",
                 "transportation_construction_and_equipment",
                 "transportation_equipment",
                 "transportation_signaling_and_control_equipment",
                 "treated_wood_foundations",
                 "tubs_and_pools",
                 "turf_and_grasses",
                 "turntables",
                 "underground_storage_tank_removal",
                 "underpinning",
                 "unit_skylights",
                 "utility_substations",
                 "value_analysis",
                 "vapor_retarders",
                 "vaults",
                 "vehicle_lifts",
                 "vehicle_service_equipment",
                 "vehicles",
                 "vehicular_access_and_parking",
                 "veneer_plastering",
                 "ventilation_hoods",
                 "vents",
                 "vertical_turbine_fire_pumps",
                 "video_surveillance",
                 "video_surveillance_positioning_equipment",
                 "video_surveillance_sensors",
                 "visual_display_units",
                 "voice_communications_switching_and_routing_equipment",
                 "wall_and_door_protection",
                 "wall_carpeting",
                 "wall_specialties",
                 "wastewater_utility_storage_tanks",
                 "water_remediation",
                 "water_repellents",
                 "water_utility_storage_tanks",
                 "water_utility_transmission_and_distribution",
                 "waterproofing",
                 "waterproofing_membrane_tiling",
                 "waterway_construction_and_equipment",
                 "weather_barriers",
                 "wetlands_restoration",
                 "wheelchair_lifts",
                 "window_hardware",
                 "window_shades",
                 "window_treatment_operating_hardware",
                 "wireless_communications_transmission_and_distribution",
                 "wood_decking",
                 "wood_doors",
                 "wood_flooring",
                 "wood_frames",
                 "wood_paneling"
             ]

    def addFilters(key,filters):
        filterString = ""
        for filter in filters:
            filterString += f"&filters[{key}]={filter}"
        return filterString

    def on_start(self):
        """Called when a simulated user starts."""
        self.token = self.get_auth_token()
        print("Hello World")

    def get_auth_token(self):
        """Function to retrieve the bearer token."""
        auth_url = os.getenv("AUTH_URL")
        payload = {
            "grant_type": "client_credentials",
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET")
        }
        response = requests.post(auth_url, json=payload)

        if response.status_code == 200:
            return response.json().get("access_token")
        else:
            raise Exception("Failed to retrieve token: {}".format(response.text))

    @task
    def get_companies(self):
        """Task to get the list of companies."""
        # Use the full URL for the GET request

        full_url = f"qualifications/rest/v1.0/companies?per_page=50&page=1"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = self.client.get(full_url, headers=headers)

        if response.status_code == 200:
            print("Successfully retrieved companies.")
        else:
            print("Failed to retrieve companies: {}".format(response.text))

    @task
    def get_companies_with_filters(self):
        filters = {
            "trades": "architectural_concrete",
            "certifications": "Certified Business Enterprise (CBE)"
        }
        full_url = f"""qualifications/rest/v1.0/companies?per_page=50&page=1
        {CompanyUser.addFilters('certifications',random.sample(CompanyUser.certifications, 3))}
        {CompanyUser.addFilters('trades',random.sample(CompanyUser.trades, 3))}"""
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = self.client.get(full_url, headers=headers)

        if response.status_code == 200:
            print("Successfully retrieved companies with filters.")
        else:
            print("Failed to retrieve companies: {}".format(response.text))

