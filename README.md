# reports-ebs-teams
This script tags all EBS based on the TRIBE and SQUAD tags in the EC2 instances and generate a report file to map which Tribes and Squads are using the instances and perhaps be able to reduce them.

As the script is all modularized with functions, the routine iterates a for over all ids volumes by doing the following routine:

- Retrieves the volume id value through the instance id.
- Retrieves the values of Tribe and Squad if they are not empty.
- Write the values of Tribe and Squad in EBS tags.
- Treat condition if the value of EBS is different from 'In use'.
- Write a file with the EBS that were and were not tagged.
- Send this file to a SLACK channel.

