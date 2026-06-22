# WT5 Antenna Controller

WT5 is the clean-start repo for the two-antenna WinTrak replacement. It keeps
the proven WT4 hardware/protocol behaviour while presenting it as a WT5 v1.0
application with clearer module boundaries for safety, tracking, calibration,
RTL power measurement, scan calibration, Y factor measurement, and logging.

## Quick Start

1. Copy `wt5.ini.example` to `wt5.ini`.
2. Edit the two antenna serial ports in `wt5.ini`.
3. Install dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. Run the GUI:

   ```bash
   python3 wt5_gui.py --config wt5.ini
   ```

## Key Safety Rules

- Elevation is always constrained to 0..90 degrees and then further constrained
  by the configured antenna limits.
- Azimuth moves use the configured allowed arc and avoid the configured
  wrap/dead-zone.
- Long slews are broken into guarded jogs and continuously polled.
- Offline, protocol, stale-position, timeout, and safety faults stop affected
  axes and are written to the event log.
- Scan files are written under `scan/`; Y factor logs are written under
  `yfactor/`; event logs are written under `logs/`.

## Architecture

- `wt5_gui.py` - Tkinter operator interface and orchestration.
- `wt5_antenna.py` - Arduino protocol, controller session, and guarded motion.
- `wt5_safety.py` - public safety facade.
- `wt5_protocol.py` - protocol facade.
- `wt5_tracking.py` - target-position helper facade.
- `wt5_calibration.py` - calibration math helpers.
- `wt5_power.py` - RTL-SDR power meter primitives.
- `wt5_config.py` - `.ini` loading/saving.
- `wt5_logging.py` - JSON-lines event log.

