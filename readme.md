# Awesome AECO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

AECO stands for Architecture, Engineering, Construction, and Operations. It refers to the integrated process of designing, building, and managing a building or infrastructure project throughout its lifecycle, from the initial design to ongoing maintenance and operations. This process involves various disciplines working together to create and manage a built environment.

> A curated list of awesome AECO resources, tools, and technologies.
> Inspired by [Awesome](https://github.com/sindresorhus/awesome).

## Contents

- [Awesome AECO](#awesome-aeco-)
  - [Contents](#contents)
  - [BIM (Building Information Modeling)](#bim-building-information-modeling)
  - [CAD (Computer-Aided Design)](#cad-computer-aided-design)
  - [Revit Plugins \& Extensions](#revit-plugins--extensions)
  - [Simulation \& Analysis](#simulation--analysis)
  - [Energy \& Sustainability](#energy--sustainability)
  - [Parametric \& Computational Design](#parametric--computational-design)
  - [IoT \& Smart Buildings](#iot--smart-buildings)
  - [Facility \& Asset Management](#facility--asset-management)
  - [Generative Design](#generative-design)
  - [Construction Automation \& Robotics](#construction-automation--robotics)
  - [AI \& Automation for AECO](#ai--automation-for-aeco)
  - [Digital Twins](#digital-twins)
  - [GIS \& Mapping](#gis--mapping)
  - [Project Management](#project-management)
  - [Cost Estimation \& Quantity Takeoff](#cost-estimation--quantity-takeoff)
  - [Contribute](#contribute)
  - [License](#license)

---

## BIM (Building Information Modeling)

- **IfcOpenShell**
  Open-source toolkit and geometry engine for BuildingSMART IFC files. Enables reading, writing, and modifying BIM models via a C++ library and Python API.
  *GitHub: [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)*

- **xBIM Toolkit**
  The eXtensible BIM Toolkit for .NET, providing libraries to work with IFC data (read, create, validate). Allows developers on the Microsoft stack to build BIM applications.
  *GitHub: [xBimTeam/XbimEssentials](https://github.com/xBimTeam/XbimEssentials)*

- **BIMserver**
  Open-source BIM server platform (Java) that stores and manages building models using IFC. Acts as a model database with versioning and multi-user collaboration.
  *GitHub: [opensourceBIM/BIMserver](https://github.com/opensourceBIM/BIMserver)*

- **IFC.js**
  JavaScript toolkit (WASM-powered) for bringing IFC BIM data into web applications. Includes `web-ifc` for fast parsing and `web-ifc-three` for viewing in Three.js.
  *GitHub: [ThatOpen/engine_web-ifc](https://github.com/ThatOpen/engine_web-ifc)*

- **That Open Engine Fragments**
  High-performance 3D engine for efficiently handling massive amounts of BIM data using the Fragments format.
  *GitHub: [ThatOpen/engine_fragment](https://github.com/ThatOpen/engine_fragment)*

- **That Open UI Components**
  Collection of web components designed for Building Information Modeling (BIM) applications.
  *GitHub: [ThatOpen/engine_ui-components](https://github.com/ThatOpen/engine_ui-components)*

- **Speckle**
  Open-source AEC data platform ("Git for BIM") that enables real-time collaboration and interoperability by streaming geometry and data between design tools.
  *GitHub: [specklesystems/speckle-server](https://github.com/specklesystems/speckle-server)*

- **BHoM (Buildings and Habitats object Model)**
  A collaborative computational framework and data schema for the built environment. Defines a core object model for AEC domains (structure, environment, MEP, etc.).
  *GitHub: [BHoM/BHoM](https://github.com/BHoM/BHoM)*

- **Revit SDK Samples**
  Revit SDK documentation and samples demonstrating Revit API usage for automation and plugin development, maintained by Autodesk's Jeremy Tammik.
  *GitHub: [jeremytammik/RevitSdkSamples](https://github.com/jeremytammik/RevitSdkSamples)*

- **BIMsurfer**
  Web-based BIM viewer for IFC models with clash detection and collaboration features.
  *GitHub: [opensourceBIM/BIMsurfer](https://github.com/opensourceBIM/BIMsurfer)*

- **GomeraX**
  Experimental IFC viewer with AI-powered BIM assistant. Features WebGL and WebGPU rendering, advanced sectioning, first-person navigation, element clustering, and natural language commands for model interaction via local LLM.
  *GitHub: [salpbes/GomeraX](https://github.com/salpbes/GomeraX)*

- **dotBIM (.bim)**
  Minimalist file format for BIM.
  *GitHub: [paireks/dotbim](https://github.com/paireks/dotbim)*

- **xeokit convert**
  Convert BIM and AEC models directly into XKT files with JavaScript for super fast loading into xeokit.
  *GitHub: [xeokit/xeokit-convert](https://github.com/xeokit/xeokit-convert)*

- **xeokit BIM Viewer**
  Bundled BIM Viewer built on top of xeokit SDK with features like measurements, tree view explorer, annotations, slicing, first-person navigation.
  *GitHub: [xeokit/xeokit-bim-viewer](https://github.com/xeokit/xeokit-bim-viewer)*

- **xeokit SDK**
  Productive open-source JavaScript SDK and 3D engine with its own WebGL renderer and extensive library of feature examples for viewing BIM, IFC, BCF, Revit, Point Clouds and other with real-world coordinates and double precision with XKT format.
  *GitHub: [xeokit/xeokit-sdk](https://github.com/xeokit/xeokit-sdk)*

- **IFClite**
  Open-source toolkit for working with IFC files in the browser, on a server, or in a desktop app. Features a WebGPU 3D viewer, IFC4/IFC4X3 support, BCF collaboration, IDS compliance checking, bSDD lookup, 2D drawing generation, and export to IFC, glTF, CSV, JSON, and Parquet.
  *GitHub: [LTplus-AG/ifc-lite](https://github.com/LTplus-AG/ifc-lite)*

- **goifc**
  Pure-Go, cgo-free IFC reader: parses STEP, walks the spatial and semantic model, tessellates geometry, and labels every quantity with where it came from (authored Qto or derived from geometry). Geometry bounds are checked against IfcOpenShell on public sample models.
  *GitHub: [blox-eng/goifc](https://github.com/blox-eng/goifc)*

- **Massing**
  Open, self-hosted, IFC-native AEC platform spanning acquisition through turnover on a single model. Browser-based IFC authoring on That Open Fragments and IfcOpenShell, federated clash detection, IDS validation, BCF round-trip, generated 2D plans, sections and elevations, a ~100-module general contracting portal with RFIs, pay apps and CPM scheduling, and a development proforma with JV waterfall.
  *GitHub: [ibuilder/massing](https://github.com/ibuilder/massing)*

- **BIM Guard**
  Open-source BIM compliance application with a FastAPI backend and Svelte frontend. Upload IFC models, extract compliance rules from regulatory documents, validate against buildingSMART IDS and ISO 19650 naming, and generate reports with BCF issues.
  *Website: [maicen.github.io](https://maicen.github.io/bim-guard/) · GitHub: [maicen/bim-guard](https://github.com/maicen/bim-guard)*

- **OpenSKP**
  Open-source toolkit for reading, writing, and converting SketchUp (`.skp`) files in five languages, with exports including GLB, OBJ, STL, PLY, DXF, IFC4, and Fragments.
  *GitHub: [iamahsanmehmood/openskp](https://github.com/iamahsanmehmood/openskp)*

- **AEC Open Source Directory**
  Curated directory of open-source projects for architecture, engineering, and construction, with a browsable live frontend.
  *Website: [directory.opensource.construction](https://directory.opensource.construction/) · GitHub: [opensource-construction/osc-directory](https://github.com/opensource-construction/osc-directory)*

- **Voxelization Toolkit**
  Toolkit for analyzing IFC building models with voxel-based geometry, including volume calculations, evacuation-distance analysis, and building-code checks.
  *GitHub: [IfcOpenShell/voxelization_toolkit](https://github.com/IfcOpenShell/voxelization_toolkit)*

- **IFC Flow Map**
  Visual, node-based tool for viewing, filtering, transforming, analyzing, and exporting IFC building data.
  *GitHub: [louistrue/ifc-flow](https://github.com/louistrue/ifc-flow)*

- **IFC Classifier**
  Browser-based tool for viewing IFC models and assigning, managing, and exporting element classifications.
  *GitHub: [louistrue/ifc-classifier](https://github.com/louistrue/ifc-classifier)*

- **HoneyIFC**
  Desktop application for browsing IFC 2x3 and IFC4 model data and exporting structured data to spreadsheets.
  *GitHub: [IliaShkola/honey-ifc](https://github.com/IliaShkola/honey-ifc)*

- **BIM Open Schema**
  Open specification for BIM data, including geometry, stored in compact Parquet-based files for data exchange and analysis.
  *GitHub: [ara3d/bim-open-schema](https://github.com/ara3d/bim-open-schema)*

- **Ara 3D WebGL**
  WebGL viewer for large building and infrastructure models represented as BIM Open Schema files.
  *GitHub: [ara3d/ara3d-webgl](https://github.com/ara3d/ara3d-webgl)*

- **Open BIM Components**
  Collection of Three.js-based tools for building browser-based BIM applications, including model processing, floor-plan navigation, and DXF export.
  *GitHub: [ThatOpen/engine_components](https://github.com/ThatOpen/engine_components)*

- **Speckle2Graph**
  Python library that converts Revit and IFC models from Speckle into Neo4j graphs while preserving model relationships and hierarchies.
  *GitHub: [regenbuild/Speckle2Graph](https://github.com/regenbuild/Speckle2Graph)*

## CAD (Computer-Aided Design)

- **FreeCAD**
  Free, open-source parametric 3D CAD modeler with a modular architecture. Includes an Arch Workbench for BIM and supports exporting to IFC, DWG, and STEP.
  *GitHub: [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD)*

- **LibreCAD**
  Open-source 2D CAD drawing tool based on QCAD's community edition. Provides a cross-platform GUI for drafting with DXF/DWG support.
  *GitHub: [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD)*

- **BRL-CAD**
  Mature open-source solid modeling system featuring a powerful CSG geometry engine and high-performance ray tracing.
  *GitHub: [BRL-CAD/brlcad](https://github.com/BRL-CAD/brlcad)*

- **OpenSCAD**
  "The Programmer's Solid 3D CAD Modeller." Users create 3D models by writing scripts that define primitives and boolean operations.
  *GitHub: [openscad/openscad](https://github.com/openscad/openscad)*

- **SolveSpace**
  A lightweight, parametric 2D/3D CAD program supporting constraint-based sketching and exports to STEP/DXF/STL.
  *GitHub: [solvespace/solvespace](https://github.com/solvespace/solvespace)*

- **CadQuery**
  Python-based parametric CAD scripting framework for mechanical and architectural design.
  *GitHub: [CadQuery/cadquery](https://github.com/CadQuery/cadquery)*

- **ArchLang**
  Open-source (MIT) DSL for floor plans that compiles `.arch` source to SVG, DXF and PDF with linting and geometric validation, and reads a plan back as rooms, areas, adjacency and an access graph without rendering an image.
  *GitHub: [ChanMeng666/archlang](https://github.com/ChanMeng666/archlang)*

- **Prompt2CAD**
  Browser-based AI CAD workspace that turns natural-language requirements into dimensioned 3D models for physical objects. Useful for early AECO components, interior fixtures, furniture, and fabrication-ready concepts with STEP, DXF, STL, OBJ, and GLB export.
  *Website: [prompt2cad.com](https://prompt2cad.com)*

- **conversion-tables**
  Exact unit conversion factors, architectural and engineering drawing scale factors, and fractional inch tables as JSON and CSV. Values derive from the legal definitions (inch, pound, US and imperial gallon) rather than being transcribed, and exact definitions are kept separate from approximate conventions. No runtime or dependencies.
  *GitHub: [Fluxcotech/conversion-tables](https://github.com/Fluxcotech/conversion-tables)*

- **Open CASCADE Technology**
  C++ platform for developing 3D surface and solid modeling, CAD data exchange, visualization, manufacturing, and numerical simulation software.
  *GitHub: [Open-Cascade-SAS/OCCT](https://github.com/Open-Cascade-SAS/OCCT)*

- **rhino3dm**
  Libraries for creating, inspecting, and exchanging Rhino geometry in .NET, Python, and JavaScript applications without requiring Rhino.
  *GitHub: [mcneel/rhino3dm](https://github.com/mcneel/rhino3dm)*

## Revit Plugins & Extensions

- **pyRevit**
  A rapid-development environment for Autodesk Revit. Lets users create custom tools in IronPython or CPython with an extensive API.
  *GitHub: [pyrevitlabs/pyRevit](https://github.com/pyrevitlabs/pyRevit)*

- **RevitLookup**
  Interactive BIM database explorer for Revit. Inspects data of selected elements (parameters, properties) in real-time.
  *GitHub: [lookup-foundation/RevitLookup](https://github.com/lookup-foundation/RevitLookup)*

- **Rhino.Inside Revit**
  Embeds McNeel Rhino 3D and Grasshopper into Revit's environment, enabling seamless transfer of geometry and parameters.
  *GitHub: [mcneel/rhino.inside-revit](https://github.com/mcneel/rhino.inside-revit)*

- **IFC Exporter for Revit**
  The open-source IFC plugin used by Revit for improved IFC support (IFC2x3/IFC4).
  *GitHub: [Autodesk/revit-ifc](https://github.com/Autodesk/revit-ifc)*

- **Revit Add-in Manager**
  Revit utility for loading, running, and debugging add-ins without restarting the application.
  *GitHub: [chuongmep/RevitAddInManager](https://github.com/chuongmep/RevitAddInManager)*

- **Bowerbird**
  Revit 2025 plugin that dynamically compiles and reloads C# command files for add-in development.
  *GitHub: [ara3d/bowerbird](https://github.com/ara3d/bowerbird)*

- **sPrint**
  Chrome extension for batch-printing PDFs and downloading derivatives from Autodesk BIM 360 and Autodesk Construction Cloud.
  *GitHub: [PerkinsAndWill-IO/sPrint](https://github.com/PerkinsAndWill-IO/sPrint)*

## Simulation & Analysis

- **EnergyPlus**
  The DOE's flagship whole-building energy simulation engine. Models heating/cooling loads, HVAC systems, and energy consumption.
  *GitHub: [NatLabRockies/EnergyPlus](https://github.com/NatLabRockies/EnergyPlus)*

- **OpenStudio**
  A cross-platform collection of tools for whole-building energy modeling that sits on top of EnergyPlus.
  *GitHub: [NatLabRockies/OpenStudio](https://github.com/NatLabRockies/OpenStudio)*

- **Ladybug Tools**
  Suite of open-source environmental analysis tools connecting CAD modeling to physics engines (e.g., Ladybug for solar analysis, Honeybee for energy/daylight).
  *GitHub: [ladybug-tools/ladybug](https://github.com/ladybug-tools/ladybug)*

- **Radiance**
  Industry-standard lighting simulation suite for evaluating daylight and electric lighting, producing accurate luminance values.
  *GitHub: [LBNL-ETA/Radiance](https://github.com/LBNL-ETA/Radiance)*

- **OpenFOAM**
  Computational fluid dynamics (CFD) toolkit for airflow and thermal simulations.
  *GitHub: [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev)*

- **OpenSees**
  Open System for Earthquake Engineering Simulation. Framework for structural FEA and seismic simulation of structures.
  *GitHub: [OpenSees/OpenSees](https://github.com/OpenSees/OpenSees)*

- **HVACLogic**
  Deterministic, 100% client-side engineering calculation suite for building science, duct aerodynamics, cooling loads, and heat pump sizing.
  *GitHub: [miadsaadidi/hvaclogic](https://github.com/miadsaadidi/hvaclogic)*

- **bim2sim**
  Python library that maps IFC BIM data into simulation models for building performance and HVAC, with basic methods for CFD and life-cycle assessment.
  *GitHub: [BIM2SIM/bim2sim](https://github.com/BIM2SIM/bim2sim)*

- **honeybee-energy**
  Honeybee extension for defining building energy properties and translating building models for EnergyPlus and OpenStudio simulation.
  *GitHub: [ladybug-tools/honeybee-energy](https://github.com/ladybug-tools/honeybee-energy)*

- **Dragonfly Core**
  Python libraries for creating and editing large-scale building models using the Dragonfly schema, with extensions for environmental simulation.
  *GitHub: [ladybug-tools/dragonfly-core](https://github.com/ladybug-tools/dragonfly-core)*

- **honeybee-radiance**
  Honeybee extension for daylight and radiation simulation with Radiance.
  *GitHub: [ladybug-tools/honeybee-radiance](https://github.com/ladybug-tools/honeybee-radiance)*

- **Awatif**
  Browser-based structural analysis and design toolset with finite-element analysis, Eurocode checks, and report generation.
  *GitHub: [madil4/awatif](https://github.com/madil4/awatif)*

## Energy & Sustainability

- **Calc**
  Revit-based workflow for assessing the environmental impact of early building designs using material assemblies and life-cycle calculations.
  *GitHub: [herzogdemeuron/calc](https://github.com/herzogdemeuron/calc)*

- **IfcLCA**
  Open-source application that analyzes building life-cycle impacts from IFC models using environmental impact data and exports results back into IFC.
  *GitHub: [IfcLCA/IfcLCA](https://github.com/IfcLCA/IfcLCA)*

- **LCAx**
  Open data format and validator for exchanging life-cycle assessment results, environmental product declarations, and assemblies.
  *GitHub: [ocni-dtu/lcax](https://github.com/ocni-dtu/lcax)*

## Parametric & Computational Design

- **Dynamo**
  Open-source visual programming platform for design automation. Popular for generative design and automating repetitive tasks in BIM.
  *GitHub: [DynamoDS/Dynamo](https://github.com/DynamoDS/Dynamo)*

- **COMPAS**
  Python-based computational framework for architecture, engineering, and digital fabrication.
  *GitHub: [compas-dev/compas](https://github.com/compas-dev/compas)*

- **Rhino.Compute**
  REST geometry server based on the Rhino 3D geometry kernel. Allows programmatic, headless access to Rhino's modeling capabilities.
  *GitHub: [mcneel/compute.rhino3d](https://github.com/mcneel/compute.rhino3d)*

- **Bonsai (formerly BlenderBIM)**
  Blender add-on for BIM workflows, supporting IFC import/export and parametric modeling.
  *GitHub: [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell/tree/HEAD/src/bonsai)*

- **Polygonjs**
  Node-based WebGL design tool for creating interactive 3D experiences and digital twins without coding.
  *GitHub: [polygonjs/polygonjs](https://github.com/polygonjs/polygonjs)*

- **COMPAS Wood**
  COMPAS-based tools for generating timber joints and working with timber fabrication geometry.
  *GitHub: [petrasvestartas/compas_wood](https://github.com/petrasvestartas/compas_wood)*

- **Geospiza**
  .NET library and Grasshopper plugin for evolutionary algorithms in architectural and engineering design.
  *GitHub: [TheVessen/geospiza](https://github.com/TheVessen/geospiza)*

- **D2P Components**
  Grasshopper plugin for organizing parametric building components, their properties, instances, and parent-child relationships.
  *GitHub: [design-to-production/D2P-Components](https://github.com/design-to-production/D2P-Components)*

- **HYWE**
  Open computational design environment for generating and analyzing early-stage architectural layouts and massing from spatial programs and constraints.
  *GitHub: [vykrum/Hywe](https://github.com/vykrum/Hywe)*

## IoT & Smart Buildings

- **Home Assistant**
  Platform for smart home automation and IoT device integration with a focus on local control and privacy.
  *GitHub: [home-assistant/core](https://github.com/home-assistant/core)*

- **openHAB**
  Vendor-agnostic open-source software for integrating and controlling smart building devices.
  *GitHub: [openhab/openhab-addons](https://github.com/openhab/openhab-addons)*

- **Eclipse VOLTTRON**
  Platform for distributed sensing and control of building systems. Provides services to collect real-time data from building equipment.
  *GitHub: [VOLTTRON/volttron](https://github.com/VOLTTRON/volttron)*

- **EdgeX Foundry**
  Modular IoT platform for managing sensors and data in smart buildings.
  *GitHub: [edgexfoundry/edgex-go](https://github.com/edgexfoundry/edgex-go)*

- **ThingsBoard**
  Open-source IoT platform for device management, data visualization, and analytics.
  *GitHub: [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard)*

- **Google Digital Buildings**
  Uniform schema and toolset for representing structured information about buildings and their installed equipment.
  *GitHub: [google/digitalbuildings](https://github.com/google/digitalbuildings)*

- **Brick Schema**
  Open-source uniform metadata schema for efficiently representing metadata in buildings.
  *GitHub: [BrickSchema/Brick](https://github.com/BrickSchema/Brick)*

## Facility & Asset Management

- **Condo**
  Open-source property management SaaS for tracking maintenance tickets, resident contacts, and fee payments.
  *GitHub: [open-condo-software/condo](https://github.com/open-condo-software/condo)*

- **Atlas CMMS**
  Self-hosted Computerized Maintenance Management System. Allows teams to schedule work orders and manage inventory.
  *GitHub: [Grashjs/cmms](https://github.com/Grashjs/cmms)*

- **FieldServiceScout**
  Independent comparisons of field-service management software for trade shops, including features and modeled true cost.
  *Website: [fieldservicescout.com](https://www.fieldservicescout.com/)*

## Generative Design

- **Anton**
  Generative design framework for Blender leveraging topology optimization as a form-finding method.
  *GitHub: [senthurayyappan/anton](https://github.com/senthurayyappan/anton)*

- **Design Explorer**
  Web application for exploring multi-dimensional design spaces, used to visualize options from parametric studies.
  *GitHub: [tt-acm/DesignExplorer](https://github.com/tt-acm/DesignExplorer)*

- **Ritn3D**
  AI floor plan to 3D interior model converter. Auto-detects walls, doors, windows, and rooms from architectural PDFs (AutoCAD, Revit, ArchiCAD, SketchUp exports), scanned blueprints, or phone-camera photos; generates a walkable 3D interior in under 2 minutes with drag-and-drop furniture and GLB / STL export.
  *Website: [ritn3d.com](https://www.ritn3d.com)*

## Construction Automation & Robotics

- **ROS (Robot Operating System)**
  Leading middleware for robotics, used in AEC to prototype construction robots or automation equipment.
  *GitHub: [ros/ros](https://github.com/ros/ros)*

- **Gazebo Simulator**
  High-fidelity 3D robotics simulator used to test construction robotics or automated equipment virtually.
  *GitHub: [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim)*

## AI & Automation for AECO

- **DDC Skills Collection for AI Coding Assistants**
  Collection of skills for AI coding assistants to automate construction workflows, including BIM analysis, cost estimation, scheduling, document processing, and reporting.
  *GitHub: [datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction)*

- **IDS MCP Server**
  Model Context Protocol server for creating, validating, and managing buildingSMART Information Delivery Specification (IDS) files.
  *GitHub: [vinnividivicci/ifc-ids-mcp](https://github.com/vinnividivicci/ifc-ids-mcp)*

## Digital Twins

- **iTwin.js**
  Open-source library from Bentley for creating and visualizing infrastructure digital twins.
  *GitHub: [iTwin/itwinjs-core](https://github.com/iTwin/itwinjs-core)*

- **PlayCanvas**
  Open-source WebGL game engine for building interactive 3D visualizations and digital twins.
  *GitHub: [playcanvas/engine](https://github.com/playcanvas/engine)*

## GIS & Mapping

- **QGIS**
  Free, open-source GIS for viewing, editing, and analyzing geospatial data.
  *GitHub: [qgis/QGIS](https://github.com/qgis/QGIS)*

- **CesiumJS**
  JavaScript library for 3D globes and map visualization, capable of streaming BIM data in a geospatial context.
  *GitHub: [CesiumGS/cesium](https://github.com/CesiumGS/cesium)*

- **OpenLayers**
  High-performance JS library for interactive maps on the web.
  *GitHub: [openlayers/openlayers](https://github.com/openlayers/openlayers)*

- **BlenderGIS**
  Blender addon to make the bridge between Blender's 3D data and 2D geographic data.
  *GitHub: [domlysz/BlenderGIS](https://github.com/domlysz/BlenderGIS)*

- **Awesome GIS**
  A curated list of GIS, remote sensing, 3D scanning, and other geospatial related sources.
  *GitHub: [sshuair/awesome-gis](https://github.com/sshuair/awesome-gis)*

## Project Management

- **OpenProject**
  Collaborative project management tool with Gantt charts, Agile workflows, and BIM integration.
  *GitHub: [opf/openproject](https://github.com/opf/openproject)*

- **LibrePlan**
  Resource planning and scheduling software for construction projects.
  *GitHub: [LibrePlan/libreplan](https://github.com/LibrePlan/libreplan)*

## Cost Estimation & Quantity Takeoff

- **BidWright**
  Open-source AI-native construction estimating: 2D/3D takeoff, assemblies, pricing, scheduling, and quotes.
  *GitHub: [braedonsaunders/bidwright](https://github.com/braedonsaunders/bidwright)*

- **Simulateur Prix Construction Maison**
  Free French-market construction cost estimator. Estimates building prices per m² based on 36 criteria and 25 budget categories (structural work, roofing, insulation, plumbing, etc.).
  *Website: [simulateur-prix-construction-maison.fr](https://simulateur-prix-construction-maison.fr/)*

- **Concrete Estimator Hub Calculators**
  Browser-based and WordPress-embeddable concrete planning calculators for slabs, bags, ready-mix comparison, and job worksheets.
  *Website: [concreteestimatorhub.com](https://concreteestimatorhub.com/) · GitHub: [xuhp630-bot/concrete-estimator-hub-calculators](https://github.com/xuhp630-bot/concrete-estimator-hub-calculators)*

- **OpenConstructionERP**
  Self-hosted construction ERP with BOQ and cost databases, PDF/CAD/BIM quantity takeoff, estimating, and 4D/5D scheduling.
  *GitHub: [datadrivenconstruction/OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP)*

## Contribute

Contributions welcome! Read the [contribution guidelines](https://github.com/osama-ata/Awesome-AECO/blob/main/contributing.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work. See [LICENSE](LICENSE).
