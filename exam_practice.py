import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
from tkinter import ttk  # Make sure to import ttk
import random
from random import shuffle

questions = [
    {
        "question": r"Which of the following is true about organizational units? (Choose all that apply.)",
        "options": [
            r"OUs can be added to an object’s DACL.",
            r"OUs can be nested.",
            r"A group policy can be linked to an OU.",
            r"Only members of Domain Administrators can work with OUs."
        ],
        "answer": [
            r"OUs can be nested.",
            r"A group policy can be linked to an OU."
        ]
    },
    {
        "question": r"You want to see the permissions set on an OU, so you open Active Directory Users and Computers, right-click the OU, and click Properties. After clicking all the available tabs, you can’t seem to find where permissions are set in the Properties dialog box. What should you do?",
        "options": [
            r"Log on as a member of Enterprise Admins and try again.",
            r"In the Properties dialog box, click the Advanced button.",
            r"Right-click the OU and click Security.",
            r"In Active Directory Users and Computers, click View, Advanced Features."
        ],
        "answer": [
            r"In Active Directory Users and Computers, click View, Advanced Features."
        ]
    },
    {
        "question": r"You have hired a new junior administrator and created an account for her with the logon name JrAdmin. You want her to be able to reset user accounts and modify group memberships for users in the Operations department whose accounts are in the Operations OU. You want to do this with the least effort and without giving JrAdmin broader capabilities. What should you do?",
        "options": [
            r"In Active Directory Administrative Center, right-click the Operations OU, click Properties, and click Managed By.",
            r"In Active Directory Users and Computers, right-click the Operations OU and click Delegate Control.",
            r"Open the Operations Security tab and add JrAdmin to the DACL.",
            r"Add JrAdmin to the Password Managers domain local group."
        ],
        "answer": [
            r"In Active Directory Users and Computers, right-click the Operations OU and click Delegate Control."
        ]
    },
    {
        "question": r"Another administrator has been changing permissions on the Operations OU by adding some groups and users to the DACL. You’re concerned that the JrAdmin account has been given more access to the OU than it should have. You need to see all permissions the JrAdmin account has to the Operations OU. What should you do?",
        "options": [
            r"In Active Directory Users and Computers, right-click the JrAdmin account, click Properties, and view her group memberships.",
            r"In Active Directory Administrative Center, run the Permissions Wizard and select JrAdmin as the target.",
            r"In Active Directory Users and Computers, enable Advanced Features, open the Operations OU’s Properties dialog box, and navigate to the Effective Access tab.",
            r"In Active Directory Administrative Center, open JrAdmin’s account properties and click the Manager Of tab."
        ],
        "answer": [
            r"In Active Directory Users and Computers, enable Advanced Features, open the Operations OU’s Properties dialog box, and navigate to the Effective Access tab."
        ]
    },
    {
        "question": r"An account named SrAdmin created an OU named QandA under the Operations OU. Which of the following is true by default?",
        "options": [
            r"Domain Admins is the owner of the QandA OU.",
            r"SrAdmin is the owner of the QandA OU and all objects created inside it.",
            r"SrAdmin has all standard permissions except Full control for the QandA OU.",
            r"The Everyone group has Read permission to the QandA OU."
        ],
        "answer": [
            r"SrAdmin is the owner of the QandA OU and all objects created inside it."
        ]
    },
    {
        "question": r"Which of the following is a user account category? (Choose all that apply.)",
        "options": [
            r"Local",
            r"Global",
            r"Domain",
            r"Universal"
        ],
        "answer": [
            r"Local",
            r"Domain"
        ]
    },
    {
        "question": r"Which of the following is a built-in user account? (Choose all that apply.)",
        "options": [
            r"Administrator",
            r"Operator",
            r"Anonymous",
            r"Guest"
        ],
        "answer": [
            r"Administrator",
            r"Guest"
        ]
    },
    {
        "question": r"Sam*Snead is a valid user account name. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"False"
        ]
    },
    {
        "question": r"Which of the following is true about user accounts in a Windows Server 2012/R2 domain? (Choose all that apply.)",
        "options": [
            r"The name can be from 1 to 20 characters.",
            r"The name is case sensitive.",
            r"The name can’t be duplicated in the domain.",
            r"Using default settings, PASSWORD123 is a valid password."
        ],
        "answer": [
            r"The name can be from 1 to 20 characters.",
            r"The name can’t be duplicated in the domain."
        ]
    },
    {
        "question": r"Which of the following account options can’t be set together? (Choose all that apply.)",
        "options": [
            r"User must change password at next logon.",
            r"Store password using reversible encryption.",
            r"Password never expires.",
            r"Account is disabled."
        ],
        "answer": [
            r"User must change password at next logon.",
            r"Password never expires."
        ]
    },
    {
        "question": r"Global groups can have domain local groups as members. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"False"
        ]
    },
    {
        "question": r"Jane has left the company. Her user account is a member of several groups and has permissions and rights to a number of forest-wide resources. Jane’s replacement will arrive in a couple of weeks and needs access to the same resources. What’s the best course of action?",
        "options": [
            r"Find all groups Jane is a member of and make a note of them. Delete Jane’s user account and create a new account for the new employee. Add the new account to all the groups Jane was a member of.",
            r"Copy Jane’s user account and give the copy another name.",
            r"Disable Jane’s account. When the new employee arrives, rename Jane’s account, assign it a new password, and enable it again.",
            r"Export Jane’s account and then import it when the new employee arrives. Rename the account and assign it a new password."
        ],
        "answer": [
            r"Disable Jane’s account. When the new employee arrives, rename Jane’s account, assign it a new password, and enable it again."
        ]
    },
    {
        "question": r"Over the past several months, Tom, who has access to sensitive company information, has logged on to computers in other departments and left them without logging off. You have discussed the matter with him, but the problem continues to occur. You’re concerned that someone could access these sensitive resources easily. What’s the best way to solve this problem?",
        "options": [
            r"Ensure that all computers Tom is logging on to have screen savers set to lock the computer after 15 minutes of inactivity.",
            r"Specify which computers Tom can log on to in the domain by using the Log On To option in his account’s properties.",
            r"Move Tom’s account and computer to another domain, thereby making it impossible for him to log on to computers that are members of different domains.",
            r"Disable local logon for Tom’s account on all computers except Tom’s."
        ],
        "answer": [
            r"Specify which computers Tom can log on to in the domain by using the Log On To option in his account’s properties."
        ]
    },
    {
        "question": r"You have noticed inappropriate use of computers for gaming and Internet downloads by some employees who come in after hours and on weekends. These employees don’t have valid work assignments during these times. You have been asked to devise a solution for these employees that doesn’t affect other employees or these employees’ computers during working hours. What’s the best solution?",
        "options": [
            r"Install personal firewall software on their computers in an attempt to block the gaming and Internet traffic.",
            r"Request that the Maintenance Department change the locks on their office doors so that they can enter only during prescribed hours.",
            r"Set the Logon Hours options for their user accounts.",
            r"Before you leave each evening and before the weekend, disable these employees’ accounts and reenable them the next working day."
        ],
        "answer": [
            r"Set the Logon Hours options for their user accounts."
        ]
    },
    {
        "question": r"The Users domain local group in the Builtin folder can be a member of the local Administrators group on a Windows client OS computer. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"False"
        ]
    },
    {
        "question": r"Which of the following is considered a security principal? (Choose all that apply.)",
        "options": [
            r"Contacts",
            r"Computer accounts",
            r"User accounts",
            r"Distribution groups"
        ],
        "answer": [
            r"Computer accounts",
            r"User accounts"
        ]
    },
    {
        "question": r"Which of the following is a valid group scope? (Choose all that apply.)",
        "options": [
            r"Global",
            r"Domain local",
            r"Forest",
            r"Domain global"
        ],
        "answer": [
            r"Global",
            r"Domain local"
        ]
    },
    {
        "question": r"What happens if a security group that’s an ACE in a shared folder is converted to a distribution group?",
        "options": [
            r"A security group can’t be converted to a distribution group if it has already been assigned permissions.",
            r"The group is removed from the DACL automatically.",
            r"The group remains in the DACL, but the ACE has no effect on members’ access to the resource.",
            r"The group remains in the DACL, and permissions assigned to the group affect access to the resource as though it were still a security group."
        ],
        "answer": [
            r"The group remains in the DACL, but the ACE has no effect on members’ access to the resource."
        ]
    },
    {
        "question": r"Which of the following can be a member of a universal group? (Choose all that apply.)",
        "options": [
            r"User accounts from the local domain only",
            r"Global groups from any domain in the forest",
            r"Other universal groups",
            r"Domain local groups from the local domain only"
        ],
        "answer": [
            r"Global groups from any domain in the forest",
            r"Other universal groups"
        ]
    },
    {
        "question": r"Which direct group scope conversion is allowed?",
        "options": [
            r"Domain local to universal, provided no domain local group is already a member",
            r"Global to domain local, without restriction",
            r"Domain local to global, provided no domain local group is already a member",
            r"Universal to global, without restriction"
        ],
        "answer": [
            r"Domain local to universal, provided no domain local group is already a member"
        ]
    },
    {
        "question": r"Which of the following is true about the Users domain local group?",
        "options": [
            r"It’s in the Users folder.",
            r"It can be converted to a global group.",
            r"Domain Users is a member.",
            r"Its members can log on locally to a domain controller."
        ],
        "answer": [
            r"Its members can log on locally to a domain controller."
        ]
    },
    {
        "question": r"A domain user logging on to the domain becomes a member of which special identity group?",
        "options": [
            r"Creator Owner",
            r"System",
            r"Authenticated Users",
            r"Anonymous Logon"
        ],
        "answer": [
            r"Authenticated Users"
        ]
    },
    {
        "question": r"Which of the following creates a file named disabled.txt containing a list of disabled Active Directory accounts?",
        "options": [
            r"net accounts /show disabled",
            r"ldifde -accounts -property=enabled -value=false",
            r"Query-Account -Disable=True | disabled.txt",
            r"Search-ADAccount -AccountDisabled > disabled.txt"
        ],
        "answer": [
            r"Search-ADAccount -AccountDisabled > disabled.txt"
        ]
    },
    {
        "question": r"A user is having trouble logging on to the domain from a computer that has been out of service for several months, and nobody else can seem to log on from the computer. What should you try first to solve the problem?",
        "options": [
            r"Reinstall Windows on the workstation and create a new computer account in the domain.",
            r"Rename the computer and create a new computer account with the new name.",
            r"Reset the computer account, remove the computer from the domain, and rejoin it to the domain.",
            r"Disable the computer account, remove the computer from the domain, and rejoin it to the domain."
        ],
        "answer": [
            r"Reset the computer account, remove the computer from the domain, and rejoin it to the domain."
        ]
    },
    {
        "question": r"Which commands can you use together to change attributes of several users at once?",
        "options": [
            r"dsget and dsadd",
            r"dsget and dsmod",
            r"dsquery and dsmod",
            r"dsquery and dsget"
        ],
        "answer": [
            r"dsquery and dsmod"
        ]
    },
    {
        "question": r"Which of the following is a local GPO on a Windows 8.1 computer? (Choose all that apply.)",
        "options": [
            r"Local Administrators",
            r"Local Default User",
            r"Local Default Domain",
            r"Local Non-Administrators"
        ],
        "answer": [
            r"Local Administrators",
            r"Local Non-Administrators"
        ]
    },
    {
        "question": r"Where is a GPT stored?",
        "options": [
            r"In a folder named the same as the GPO in the SYSVOL share",
            r"In a folder named the same as the GUID of the GPO in Active Directory",
            r"In a folder named the same as the GUID of the GPO in the SYSVOL share",
            r"In a folder named the same as the GPO in Active Directory"
        ],
        "answer": [
            r"In a folder named the same as the GUID of the GPO in the SYSVOL share"
        ]
    },
    {
        "question": r"A user-specific local GPO takes precedence over a site-linked GPO. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"False"
        ]
    },
    {
        "question": r"You’re having replication problems with your GPOs and suspect that the version numbers have somehow gotten out of sync between the GPT and the GPC. What can you do to verify the version numbers on a GPO?",
        "options": [
            r"Check the versionNumber attribute of the GPC and open the GPT.INI file.",
            r"Check the versionNumber attribute of the GPT and open the GPC.INI file.",
            r"Right-click the GPO in the Group Policy Management console, click Properties, and view the version in the General tab.",
            r"Right-click the GPO in the Group Policy Management Editor, click Properties, and view the version in the General tab."
        ],
        "answer": [
            r"Check the versionNumber attribute of the GPC and open the GPT.INI file."
        ]
    },
    {
        "question": r"All your domain controllers are running Windows Server 2012 R2. You’re noticing problems with GPT replication. What should you check?",
        "options": [
            r"Verify that Active Directory replication is working correctly.",
            r"Verify that FRS is operating correctly.",
            r"Verify that DFSR is operating correctly.",
            r"Check the GPOReplication flag for the GPT in the Attribute Editor."
        ],
        "answer": [
            r"Verify that DFSR is operating correctly."
        ]
    },
    {
        "question": r"Which of the following is an inbound and outbound rule type you can create with Windows Firewall with Advanced Security? (Choose all that apply.)",
        "options": [
            r"Program",
            r"Port",
            r"Server",
            r"Isolation"
        ],
        "answer": [
            r"Program",
            r"Port"
        ]
    },
    {
        "question": r"You have created a GPO that defines settings only in the Local Policies node. You want the settings to apply to all computers in the domain and take precedence over any other GPOs. Which of the following is the best approach?",
        "options": [
            r"Link the new GPO to the domain, and unlink the Default Domain Policy. Right-click the domain object and click Enforced.",
            r"Link the new GPO to each OU containing computer accounts, and make sure it has link order 1.",
            r"Link the new GPO to the domain, and then right-click the new GPO and click Enforced.",
            r"Link the new GPO to the domain, make sure it has the highest link order, and then right-click the domain object and click Block Inheritance."
        ],
        "answer": [
            r"Link the new GPO to the domain, and then right-click the new GPO and click Enforced."
        ]
    },
    {
        "question": r"Which of the following represents the correct order in which GPOs are applied to an object that falls within the GPO’s scope?",
        "options": [
            r"Site, domain, OU, local GPOs",
            r"Local GPOs, domain, site, OU",
            r"Domain, site, OU, local GPOs",
            r"Local GPOs, site, domain, OU"
        ],
        "answer": [
            r"Local GPOs, site, domain, OU"
        ]
    },
    {
        "question": r"Your network consists of three sites and two domains, with some computers from both domains at each site. Each site has certain security settings that should apply to all computers from both domains when they’re located at the site. What’s the best way to ensure that the correct security settings are applied to the computers at each site?",
        "options": [
            r"Create three OUs in each domain, one for each site. In both domains, place the computer accounts in the OU corresponding to the site where the computer is located. Apply a GPO with the appropriate security settings to each OU in both domains.",
            r"Create three GPOs, one for each site, with the appropriate security settings. Apply the GPOs to the corresponding site, and enforce the GPO.",
            r"Create three GPOs, one for each site. Apply the GPOs to the domain object in both domains. Create three groups, one for each site, and place the computer accounts in the appropriate groups. Use GPO filtering to make sure the policy configured for each site affects only the corresponding group of computers.",
            r"On each computer in each site, configure the local GPO in GPOE with the appropriate security settings. In the Group Policy Object Editor, right-click the Computer Configuration node and click Block Inheritance."
        ],
        "answer": [
            r"Create three GPOs, one for each site, with the appropriate security settings. Apply the GPOs to the corresponding site, and enforce the GPO."
        ]
    },
    {
        "question": r"Objects in an OU with the Block Inheritance option set are affected by a domain-linked GPO with the Enforced option set. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"True"
        ]
    },
    {
        "question": r"You have created a GPO named RestrictU and linked it to the Operations OU (containing 30 users) with link order 3. RestrictU sets several policies in the User Configuration node. After a few days, you realize the Operations OU has three users who should be exempt from the restrictions in this GPO. You need to make sure these three users are exempt from RestrictU’s settings, but all other policy settings are still in effect for them. What’s the best way to proceed?",
        "options": [
            r"Move the three users to a new OU. Create a GPO with settings appropriate for the three users, and link it to the new OU.",
            r"Create an OU under Operations, and move the three users to this new OU. Create a GPO, and link it to this new OU. Configure the new OU to block inheritance of the RestrictU GPO.",
            r"Create a global group and add the three users as members. Configure GPO security filtering so that the global group is denied access to the GPO.",
            r"Set the Enforced option on RestrictU with an Enforce filter that excludes the three user accounts."
        ],
        "answer": [
            r"Create a global group and add the three users as members. Configure GPO security filtering so that the global group is denied access to the GPO."
        ]
    },
    {
        "question": r"You want to make changes to policy settings that affect File Explorer. The settings are in the Administrative Templates folder of the User Configuration node. You want the settings to affect all users in the domain. Which of the following is the best way to accomplish this?",
        "options": [
            r"Create a GPO, configure the policy, and link the GPO to the Domain object.",
            r"Create a GPO, configure the policy, and link the GPO to the Users OU.",
            r"Configure the policy in the Default Domain Controllers Policy GPO.",
            r"Configure the policy in the Default Domain Policy GPO and set a security filter for the Domain Users group."
        ],
        "answer": [
            r"Create a GPO, configure the policy, and link the GPO to the Domain object."
        ]
    },
    {
        "question": r"In Active Directory, all your computer accounts are in the Computers folder, and all your user accounts are in the Users folder. You need to configure an AppController policy that affects users who log on to computers in the Engineering Department. Which of the following is the best way to accomplish this?",
        "options": [
            r"Place the Engineering Department user accounts in a group. Create a new GPO, configure the AppController policy, and link the GPO to the group you created.",
            r"Place the Engineering Department computer accounts in a group named Eng. Create a new GPO, configure the AppController policy, and link it to the domain object. Set a security filter for the Eng group.",
            r"Move the Engineering Department user accounts to a new OU named Eng. Configure the AppController policy on the Default Domain Policy GPO. Set Block Inheritance on the Users folder.",
            r"Move the Engineering Department computer accounts to a new OU named Eng. Create a new GPO, configure the AppController policy, and link the GPO to the Eng OU."
        ],
        "answer": [
            r"Move the Engineering Department computer accounts to a new OU named Eng. Create a new GPO, configure the AppController policy, and link the GPO to the Eng OU."
        ]
    },
    {
        "question": r"You have been working with ADMX files to modify existing Administrative Templates and create new templates. You work on different domain controllers, depending on your location. Despite a concerted effort, your ADMX files are getting out of sync. How can you solve this problem?",
        "options": [
            r"Remove group policy management tools from all but one domain controller so that policies can be managed from only one computer.",
            r"Create an ADMX store in the SYSVOL share, and copy the ADMX files to the ADMX store.",
            r"Create an ADMX store in Active Directory, and move all your ADMX files to Active Directory.",
            r"Share the %systemroot%\PolicyDefinitions folder on all your domain controllers, and set up Task Scheduler to copy ADMX files automatically from one system to all other systems."
        ],
        "answer": [
            r"Create an ADMX store in the SYSVOL share, and copy the ADMX files to the ADMX store."
        ]
    },
    {
        "question": r"What Group Policy feature should you use if you have a policy linked to an OU that contains computer accounts but want the policy to affect only computers running Windows 7? You don’t know exactly which computer accounts represent the computers running Windows 7.",
        "options": [
            r"Disabling inheritance",
            r"Policy enforcement",
            r"WMI filtering",
            r"Security filtering"
        ],
        "answer": [
            r"WMI filtering"
        ]
    },
    {
        "question": r"You’re concerned that some domain controllers and workstations don’t meet security requirements. What should you do to verify security settings on a computer against a list of known settings?",
        "options": [
            r"Create a security template and run Group Policy Modeling.",
            r"Create a security database from a template and run secedit.exe.",
            r"Load the Security Templates snap-in and use the Group Policy Results feature.",
            r"Export the Security Settings node on the computer and run Security Configuration and Analysis."
        ],
        "answer": [
            r"Export the Security Settings node on the computer and run Security Configuration and Analysis."
        ]
    },
    {
        "question": r"None of the computers in an OU seem to be getting computer policies from the GPO linked to the OU, but users in the OU are getting user policies from this GPO. Which of the following is a possible reason that computer policies in the GPO aren’t affecting the computers? (Choose all that apply.)",
        "options": [
            r"The GPO link is disabled.",
            r"The Computer Configuration settings are disabled.",
            r"The computer accounts have Deny Read permission.",
            r"The OU has the Block Inheritance option set."
        ],
        "answer": [
            r"The Computer Configuration settings are disabled.",
            r"The computer accounts have Deny Read permission."
        ]
    },
    {
        "question": r"Which of the following sets the profile for each network connection on your computer?",
        "options": [
            r"The Network Connection policy under the Software Settings node",
            r"The Windows Firewall with Advanced Security policy",
            r"The Properties dialog box of each network interface",
            r"The Network Location Awareness feature"
        ],
        "answer": [
            r"The Network Location Awareness feature"
        ]
    },
    {
        "question": r"You want to configure an inbound firewall rule that allows a connection only if the computer trying to make the connection is authenticated. What option should you select?",
        "options": [
            r"Allow the connection if it is secure",
            r"Block unauthenticated connections",
            r"Isolation mode",
            r"Allow Domain connections"
        ],
        "answer": [
            r"Allow the connection if it is secure"
        ]
    },
    {
        "question": r"You want to configure an encrypted and authenticated connection between two gateway computers. What rule type should you configure in the New Connection Security Rule Wizard?",
        "options": [
            r"Isolation",
            r"Server-to-server",
            r"Tunnel",
            r"Authentication exemption"
        ],
        "answer": [
            r"Tunnel"
        ]
    },
    {
        "question": r"You want to create policies in a new GPO that affects only computers with Windows 7 installed. You don’t want to reorganize your computer accounts to do this, and you want computers that are upgraded to Windows 8.1 to fall out of the GPO’s scope automatically. What can you do?",
        "options": [
            r"For each policy, use selective application to specify Windows 7 as the OS.",
            r"Create a new OU, place all computer accounts representing computers with Windows 7 installed in this OU, and link the GPO to this OU.",
            r"Create a group called W7Computers. Place all computer accounts representing computers with Windows 7 installed in this group, and use this group in a security filter on the GPO. Link the GPO to the domain.",
            r"Configure a WMI filter on the GPO that specifies Windows 7 as the OS. Link the GPO to the domain."
        ],
        "answer": [
            r"Configure a WMI filter on the GPO that specifies Windows 7 as the OS. Link the GPO to the domain."
        ]
    },
    {
        "question": r"When a policy setting in Computer Configuration and User Configuration in the same GPO conflict, the Computer Configuration policy setting takes precedence. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"True"
        ]
    },
    {
        "question": r"You’re a consultant for a small company that uses eight Windows 8.1 computers in a workgroup configuration. The owner asked you to set restrictive policies on users to prevent them from making Control Panel, desktop, and other changes. The owner wants to be exempt from these policies but shouldn’t be a member of the local Administrators group. What should you do?",
        "options": [
            r"Configure the Local Computer Policy object, and then configure a user-specific GPO for the owner.",
            r"Configure the Local Computer Policy object, and use GPO filtering to exempt the owner from this policy.",
            r"Install Windows Server 2012 R2 and configure Active Directory. Add the Vista computers to the domain, configure a GPO for the domain, and use filtering to exempt the owner.",
            r"Configure the Local Computer Policy object, and then configure a logon script for the owner that changes the restrictive settings."
        ],
        "answer": [
            r"Configure the Local Computer Policy object, and use GPO filtering to exempt the owner from this policy."
        ]
    },
    {
        "question": r"You want to have a library of GPOs that specify baseline settings for different policy categories, and you can use this library to create new GPOs with baseline settings already configured. What’s the best way to accomplish this?",
        "options": [
            r"Create a number of GPOs in the Group Policy Objects folder and export the settings.",
            r"Create Starter GPOs for each policy category you want to configure.",
            r"Configure the GPOs in the Group Policy Modeling folder.",
            r"Create GPOs in offline mode and save them to the central store."
        ],
        "answer": [
            r"Create Starter GPOs for each policy category you want to configure."
        ]
    },
    {
        "question": r"Which type of connection security rule should you configure if you want to prevent computers in your domain from connecting to computers outside the domain?",
        "options": [
            r"Isolation",
            r"Authentication exemption",
            r"Server-to-server",
            r"Tunnel"
        ],
        "answer": [
            r"Isolation"
        ]
    },
    {
        "question": r"Which of the following best describes DNS? (Choose all that apply.)",
        "options": [
            r"Hierarchical database",
            r"Flat database",
            r"Monolithic database",
            r"Distributed database"
        ],
        "answer": [
            r"Hierarchical database",
            r"Distributed database"
        ]
    },
    {
        "question": r"Which of the following accurately represents an FQDN?",
        "options": [
            r"host.top-level-domain.subdomain.domain",
            r"domain.host.top-level-domain",
            r"host.subdomain.domain.top-level-domain",
            r"host.domain.top-level-domain.subdomain"
        ],
        "answer": [
            r"host.subdomain.domain.top-level-domain"
        ]
    },
    {
        "question": r"A DNS server that can’t resolve a query from its local data sends a recursive query to a root server. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"True"
        ]
    },
    {
        "question": r"A resource record containing an alias for another record is which of the following record types?",
        "options": [
            r"A",
            r"CNAME",
            r"NS",
            r"PTR"
        ],
        "answer": [
            r"CNAME"
        ]
    },
    {
        "question": r"What type of resource record is necessary to get a positive response from the command nslookup 192.168.100.10?",
        "options": [
            r"A",
            r"CNAME",
            r"NS",
            r"PTR"
        ],
        "answer": [
            r"PTR"
        ]
    },
    {
        "question": r"When a DNS server responds to a query with a list of name servers, what is the response called?",
        "options": [
            r"Iterative",
            r"Recursive",
            r"Referral",
            r"Resolver"
        ],
        "answer": [
            r"Referral"
        ]
    },
    {
        "question": r"You’re scanning the local cache on a DNS client, and you come across the notation ::1. What does it mean?",
        "options": [
            r"The cache is corrupt.",
            r"It’s the IPv6 localhost address.",
            r"It’s the link-local address.",
            r"It’s a reverse lookup record."
        ],
        "answer": [
            r"It’s the IPv6 localhost address."
        ]
    },
    {
        "question": r"Your company just opened a small branch office where 10 computer users will work. You have installed a single Windows Server 2012 R2 computer configured as a member server for basic file and print server needs. Users require DNS for Internet access and to resolve names of company resources. You decide to install DNS on the existing server. Which of the following types of installations makes the most sense?",
        "options": [
            r"A primary server hosting a standard zone",
            r"An Active Directory–integrated zone hosting the zone in which the server is a member",
            r"A caching-only DNS server",
            r"A server that’s a forwarder"
        ],
        "answer": [
            r"A caching-only DNS server"
        ]
    },
    {
        "question": r"You have a DNS server outside your corporate firewall that’s a stand-alone Windows Server 2012 R2 server. It hosts a primary zone for your public Internet domain name, which is different from your internal Active Directory domain names. You want one or more of your internal servers to be able to handle DNS queries for your public domain and to serve as a backup for the primary DNS server outside the firewall. Which configuration should you choose for internal DNS servers?",
        "options": [
            r"Configure a standard secondary zone.",
            r"Configure a standard stub zone.",
            r"Configure a forwarder to point to the primary DNS server.",
            r"Configure an Active Directory–integrated stub zone."
        ],
        "answer": [
            r"Configure a standard secondary zone."
        ]
    },
    {
        "question": r"DNS ServerA forwards a query to ForwarderB, which replies with a “not found” message. DNS ServerA continues the lookup by querying a root server. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"False"
        ]
    },
    {
        "question": r"Which of the following is true about stub zones? (Choose all that apply.)",
        "options": [
            r"They’re authoritative for the zone.",
            r"Their records are updated by the primary server automatically.",
            r"They can’t be Active Directory integrated.",
            r"They contain SOA and NS records."
        ],
        "answer": [
            r"Their records are updated by the primary server automatically.",
            r"They contain SOA and NS records."
        ]
    },
    {
        "question": r"You have Windows Server 2012 R2 DNS servers, Windows Server 2008 DNS servers, and two old Windows 2000 DNS servers in a Windows domain. You just created a new zone, newzone.com, that you want replicated by Active Directory to all DNS servers. Where should you store the zone?",
        "options": [
            r"ForestDNSZones partition",
            r"Newzone.com.dns",
            r"DomainDNSZones partition",
            r"Domain partition"
        ],
        "answer": [
            r"DomainDNSZones partition"
        ]
    },
    {
        "question": r"The DNS server at your headquarters holds a standard primary zone for the abc.com domain. A branch office connected by a slow WAN link holds a secondary zone for abc.com. Updates to the zone aren’t frequent. How can you decrease the amount of WAN traffic caused by the secondary zone checking for zone updates?",
        "options": [
            r"In the SOA tab of the zone’s Properties dialog box, increase the minimum (default) TTL.",
            r"In the Advanced tab of the DNS server’s Properties dialog box, increase the expire interval.",
            r"In the SOA tab of the zone’s Properties dialog box, increase the refresh interval.",
            r"In the Zone Transfers tab of the SOA Properties dialog box, decrease the retry interval."
        ],
        "answer": [
            r"In the SOA tab of the zone’s Properties dialog box, increase the refresh interval."
        ]
    },
    {
        "question": r"What type of record does DNS create automatically to resolve the FQDN of an NS record?",
        "options": [
            r"PTR records",
            r"CNAME records",
            r"Glue A records",
            r"Auto SRV records"
        ],
        "answer": [
            r"Glue A records"
        ]
    },
    {
        "question": r"You want a DNS server to handle queries for a domain with a standard primary zone hosted on another DNS server, and you don’t want the server to be authoritative for that zone. How should you configure the server? (Choose all that apply.)",
        "options": [
            r"Configure a secondary zone on the DNS server.",
            r"Configure a stub zone on the DNS server.",
            r"Configure a forwarder on the DNS server.",
            r"Configure zone hints for the primary zone."
        ],
        "answer": [
            r"Configure a stub zone on the DNS server.",
            r"Configure a forwarder on the DNS server."
        ]
    },
    {
        "question": r"You’re in charge of a standard primary zone for a large network with frequent changes to the DNS database. You want changes to the zone to be transmitted as quickly as possible to all secondary servers. What should you configure and on which server?",
        "options": [
            r"Configure DNS notifications on the primary zone server.",
            r"Configure DNS recursion on the secondary zone servers.",
            r"Configure round robin on the primary zone server.",
            r"Configure a smaller default TTL for the primary zone server."
        ],
        "answer": [
            r"Configure DNS notifications on the primary zone server."
        ]
    },
    {
        "question": r"You have several hundred client computers using WINS to resolve names of some enterprise servers. Many of the client computers are laptops used to connect to the network remotely. You’re trying to eliminate WINS from your network to reduce the number of protocols and services you must support. What can you do, with the least administrative effort, that allows you to stop using WINS yet still allows clients computers to use a single-label name for accessing enterprise servers?",
        "options": [
            r"Create a GlobalNames zone and add CNAME records for enterprise servers.",
            r"Create a Hosts file containing servers’ names and addresses and upload this file to each client that needs it.",
            r"Configure each client computer with the correct domain suffix.",
            r"Create a stub zone and add CNAME records for each enterprise server."
        ],
        "answer": [
            r"Create a GlobalNames zone and add CNAME records for enterprise servers."
        ]
    },
    {
        "question": r"You manage the DNS structure on your network. The network security group has decided that only one DNS server should contact the Internet. Under no circumstances should other servers contact the Internet for DNS queries, even if the designated server is down. You have decided that the DNS server named DNS-Int should be the server allowed to contact the Internet. How should you configure your DNS structure to accommodate these requirements?",
        "options": [
            r"On each DNS server except DNS-Int, configure a forwarder pointing to DNS-Int. Configure DNS-Int as a forwarder by enabling forwarded requests in the Forwarders tab of the server’s Properties dialog box.",
            r"On each DNS server except DNS-Int, configure a root hint to point to DNS-Int and delete all other root hints. Configure a root zone on DNS-Int.",
            r"On each DNS server except DNS-Int, configure a forwarder pointing to DNS-Int. Disable the use of root hints if no forwarders are available. No changes are necessary on DNS-Int.",
            r"On each DNS server except DNS-Int, in the Advanced tab of the server’s Properties dialog box, disable recursion. No changes are necessary for DNS-Int."
        ],
        "answer": [
            r"On each DNS server except DNS-Int, configure a forwarder pointing to DNS-Int. Disable the use of root hints if no forwarders are available. No changes are necessary on DNS-Int."
        ]
    },
    {
        "question": r"You have a zone containing two A records for the same hostname, but each A record has a different IP address configured. The host records point to two servers hosting a high-traffic Web site, and you want the servers to share the load. After some testing, you find that you’re always accessing the same Web server, so load sharing isn’t occurring. What can you do to solve the problem?",
        "options": [
            r"Enable the load sharing option on the zone.",
            r"Enable the round robin option on both A records.",
            r"Enable the load sharing option on both A records.",
            r"Enable the round robin option on the server."
        ],
        "answer": [
            r"Enable the round robin option on the server."
        ]
    },
    {
        "question": r"Which is the correct order in which a DNS client tries to resolve a name?",
        "options": [
            r"Cache, DNS server, Hosts file",
            r"Hosts file, cache, DNS server",
            r"Cache, Hosts file, DNS server",
            r"DNS server, cache, Hosts file"
        ],
        "answer": [
            r"Hosts file, cache, DNS server"
        ]
    },
    {
        "question": r"You want to verify whether a PTR record exists for the server1.csmtech.local host, but you don’t know the server’s IP address. Which of the following commands should you use to see whether a PTR record exists for server1.csmtech.local?",
        "options": [
            r"ping -a server1.csmtech.local, and then ping IPAddress returned from the first ping",
            r"nslookup server1.csmtech.local, and then nslookup IPAddress returned from the first nslookup",
            r"dnscmd /PTR server1.csmtech.local",
            r"dnslint /PTR server1.csmtech.local"
        ],
        "answer": [
            r"nslookup server1.csmtech.local, and then nslookup IPAddress returned from the first nslookup"
        ]
    },
    {
        "question": r"You have two DCs, each with three Active Directory–integrated zones. You’re getting inconsistent DNS lookup results and suspect a problem with Active Directory replication. What tool can you use to investigate the problem? (Choose all that apply.)",
        "options": [
            r"nslookup",
            r"dnscmd",
            r"dcdiag",
            r"ipconfig"
        ],
        "answer": [
            r"dcdiag"
        ]
    },
    {
        "question": r"To resolve a query, a DNS server looks in its local cache first. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"True"
        ]
    },
    {
        "question": r"You have just finished setting up your DNS infrastructure, and the DNS process seems to be working well. You want to be able to create a baseline of performance data so that if slowdowns occur later, you have information for comparison purposes. Which tool should you use?",
        "options": [
            r"dnscmd.exe",
            r"Debug logging",
            r"Performance Monitor",
            r"Event logging"
        ],
        "answer": [
            r"Performance Monitor"
        ]
    },
    {
        "question": r"You’re having trouble with logons and other domain operations in your domain named csmtech.local. You want to verify that your domain clients can find domain controllers. Which of the following can you do? (Choose all that apply.)",
        "options": [
            r"Use the dcdiag /test:dns /DnsRecordRegistration command.",
            r"Look at the %systemroot%\System32\Config\netlogon.dns file.",
            r"Look at the %systemroot%\System32\dns\cache.dns file.",
            r"Use the nslookup -type = CNAME -domain=csmtech.local command."
        ],
        "answer": [
            r"Use the dcdiag /test:dns /DnsRecordRegistration command.",
            r"Look at the %systemroot%\System32\Config\netlogon.dns file."
        ]
    },
    {
        "question": r"Which of the following is true about the DHCP protocol? (Choose all that apply.)",
        "options": [
            r"There are eight message types.",
            r"DHCPDISCOVER messages sent by clients traverse routers.",
            r"It uses the UDP Transport-layer protocol.",
            r"An initial address lease involves three packets."
        ],
        "answer": [
            r"There are eight message types.",
            r"It uses the UDP Transport-layer protocol."
        ]
    },
    {
        "question": r"You have a DHCP server set up on your network and no DHCP relay agents. You’re capturing DHCP packets with a protocol analyzer and see a broadcast packet with UDP source port 68 and UDP destination port 67. Which of the following DHCP message types can the packet be?",
        "options": [
            r"A DHCPREQUEST to renew an IP address lease",
            r"A DHCPACK to acknowledge an IP address lease request",
            r"A DHCPDISCOVER to request an IP address",
            r"A DHCPOFFER to offer an IP address lease"
        ],
        "answer": [
            r"A DHCPDISCOVER to request an IP address"
        ]
    },
    {
        "question": r"In the DHCP server’s statistics, you notice that a lot of DHCPNAK packets have been transmitted. What’s the most likely reason?",
        "options": [
            r"You changed the range of addresses in a scope recently.",
            r"The DHCP server has been taken offline.",
            r"The server is offering a lot of addresses that are already in use.",
            r"Client computers are getting multiple offers when they request an address."
        ],
        "answer": [
            r"You changed the range of addresses in a scope recently."
        ]
    },
    {
        "question": r"You have configured your computers with static IP addresses but want them to get the DNS server and default gateway settings via DHCP. What type of DHCP message do you see as a result?",
        "options": [
            r"DHCPREQUEST",
            r"DHCPRELEASE",
            r"DHCPNAK",
            r"DHCPINFORM"
        ],
        "answer": [
            r"DHCPINFORM"
        ]
    },
    {
        "question": r"After you install the DHCP Server role on a member server, what must you do before the server can begin providing DHCP services?",
        "options": [
            r"Configure options.",
            r"Activate the server.",
            r"Authorize the server.",
            r"Create a filter."
        ],
        "answer": [
            r"Authorize the server."
        ]
    },
    {
        "question": r"Which of the following is a required element of a DHCP scope? (Choose all that apply.)",
        "options": [
            r"Subnet mask",
            r"Scope name",
            r"Router address",
            r"Lease duration"
        ],
        "answer": [
            r"Subnet mask",
            r"Lease duration"
        ]
    },
    {
        "question": r"What’s the default lease duration on a Windows DHCP server?",
        "options": [
            r"8 hours",
            r"16 minutes",
            r"8 days",
            r"16 hours"
        ],
        "answer": [
            r"8 days"
        ]
    },
    {
        "question": r"IP addresses can be leased for an unlimited period. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"True"
        ]
    },
    {
        "question": r"What should you define in a scope to prevent the DHCP server from leasing addresses that are already assigned to devices statically?",
        "options": [
            r"Reservation scope",
            r"Exclusion range",
            r"Deny filters",
            r"DHCP policy"
        ],
        "answer": [
            r"Exclusion range"
        ]
    },
    {
        "question": r"You have four printers that are accessed via their IP addresses. You want to be able to use DHCP to assign addresses to the printers, but you want to make sure they always have the same address. What’s the best option?",
        "options": [
            r"Create reservations.",
            r"Create exclusions.",
            r"Configure filters.",
            r"Configure policies."
        ],
        "answer": [
            r"Create reservations."
        ]
    },
    {
        "question": r"A DHCP server can serve clients from only one subnet. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"False"
        ]
    },
    {
        "question": r"You have defined a scope on your DHCP server with the start address 172.16.1.1, end address 172.16.1.200, and prefix length 16. You want to create another scope on the server. Which of the following is a valid scope you can create on this server?",
        "options": [
            r"Start address 172.19.1.1, end address 172.19.1.255, prefix length 24",
            r"Start address 172.17.1.1, end address 172.17.1.200, prefix length 16",
            r"Start address 172.16.2.1, end address 172.19.2.100, prefix length 16",
            r"Start address 172.31.0.1, end address 172.31.1.254, prefix length 8"
        ],
        "answer": [
            r"Start address 172.19.1.1, end address 172.19.1.255, prefix length 24"
        ]
    },
    {
        "question": r"You want high availability for DHCP services, a primary server to handle most DHCP requests, and a secondary server to respond to client requests only if the primary server fails to in about a second. The primary server has about 85% of the IP addresses to lease, leaving the secondary server with about 15%. You don’t want the servers to replicate with each other. What should you configure?",
        "options": [
            r"Multicast scope",
            r"Failover",
            r"Superscope",
            r"Split scope"
        ],
        "answer": [
            r"Split scope"
        ]
    },
    {
        "question": r"A subnet on your network uses DHCP for address assignment. The current scope has start address 192.168.1.1 and end address 192.168.1.200 with the subnet mask 255.255.255.0. Because of network expansion, you have added computers, bringing the total number that needs DHCP for address assignment to 300. You don’t want to change the IP addressing scheme or the subnet mask for computers already on the network. What should you do?",
        "options": [
            r"Create a new scope with start address 192.168.2.1 and end address 192.168.2.200 with prefix length 24 and add the existing scope and new scope to a superscope.",
            r"Add a scope with start address 192.168.1.1 and end address 192.168.2.200 with the subnet mask 255.255.255.0. Then delete the existing scope.",
            r"Create a new scope with start address 192.168.1.1, end address 192.168.2.200, and prefix length 16.",
            r"Add another DHCP server. Using the split scope wizard, split the existing scope with the new server and assign each server 100% of the addresses."
        ],
        "answer": [
            r"Create a new scope with start address 192.168.2.1 and end address 192.168.2.200 with prefix length 24 and add the existing scope and new scope to a superscope."
        ]
    },
    {
        "question": r"Server options take precedence over scope options. True or False?",
        "options": [
            r"True",
            r"False"
        ],
        "answer": [
            r"False"
        ]
    },
    {
        "question": r"You want mobile devices on your network to have a shorter lease time than other devices without having a different scope. You don’t have detailed information about the mobile devices, such as MAC addresses, because they are employees’ personal devices. What DHCP feature might you use to assign a shorter lease to these mobile devices?",
        "options": [
            r"Reservation options",
            r"Scope options",
            r"Policy options",
            r"Filter options"
        ],
        "answer": [
            r"Policy options"
        ]
    },
    {
        "question": r"You have DHCP clients on the network that aren’t domain members. You want to be sure these computers can register their hostnames with your DNS servers. Which option should you configure?",
        "options": [
            r"003 Router",
            r"044 WINS/NBNS Servers",
            r"006 DNS Servers",
            r"015 DNS Domain name"
        ],
        "answer": [
            r"015 DNS Domain name"
        ]
    },
    {
        "question": r"You want all computers in the Management Department to use a default gateway that’s different from computers in other departments. All departments are on the same subnet. What should you do first on the server?",
        "options": [
            r"Create a User Class.",
            r"Create a new scope.",
            r"Create an allow filter.",
            r"Create a Vendor Class."
        ],
        "answer": [
            r"Create a User Class."
        ]
    },
    {
        "question": r"You have a DHCP server with two NICs: NIC1 and NIC2. NIC1 is connected to a subnet with computers that use DHCP for address assignment. NIC2 is connected to the data center subnet, where all computers should use static addressing. You want to prevent the DHCP server from listening for DHCP packets on NIC2. What should you do?",
        "options": [
            r"Configure bindings.",
            r"Disable the scope.",
            r"Create a filter for NIC2.",
            r"Configure failover."
        ],
        "answer": [
            r"Configure bindings."
        ]
    },
    {
        "question": r"You notice that some information shown in the DHCP console for DHCP leases doesn’t agree with lease information you see on some client computers where you used ipconfig /all. What should you do to make DHCP information consistent?",
        "options": [
            r"Back up and restore the database.",
            r"Reconcile the scopes.",
            r"Create a deny filter for the leases that look wrong.",
            r"Delete the dhcp.mdb file and click Refresh."
        ],
        "answer": [
            r"Reconcile the scopes."
        ]
    },
    {
        "question": r"Some of your non-Windows clients aren’t registering their hostnames with the DNS server. You don’t require secure updates on the DNS server. What option should you configure on the DHCP server so that non-Windows clients names are registered?",
        "options": [
            r"Update DNS records dynamically only if requested by the DHCP clients.",
            r"Always dynamically update DNS records.",
            r"Update DNS records dynamically for DHCP clients that don’t request updates.",
            r"Configure name protection."
        ],
        "answer": [
            r"Update DNS records dynamically for DHCP clients that don’t request updates."
        ]
    },
    {
        "question": r"You’re reviewing DHCP server statistics and notice that the server has received many DHCPDECLINE messages. What should you configure on the server to reduce the number of DHCPDECLINE messages?",
        "options": [
            r"DHCP policies",
            r"Conflict detection",
            r"Connection bindings",
            r"DNS credentials"
        ],
        "answer": [
            r"Conflict detection"
        ]
    },
    {
        "question": r"You have a network of 150 computers and notice that a computer you don’t recognize has been leasing an IP address. You want to make sure this computer can’t lease an address from your server. What’s the best solution that takes the least administrative effort?",
        "options": [
            r"Create an allow filter.",
            r"Create a new policy.",
            r"Create a deny filter.",
            r"Create a Vendor Class."
        ],
        "answer": [
            r"Create a deny filter."
        ]
    },
    {
        "question": r"Which of the following is a criterion you can use with conditions in DHCP policies? (Choose all that apply.)",
        "options": [
            r"Vendor Class",
            r"MAC address",
            r"OS version",
            r"SSID"
        ],
        "answer": [
            r"Vendor Class",
            r"MAC address"
        ]
    },
    {
        "question": r"Why might you need to create predefined options with code 060?",
        "options": [
            r"To support WSUS clients",
            r"To support Linux clients",
            r"To support WDS clients",
            r"To support mobile clients"
        ],
        "answer": [
            r"To support WDS clients"
        ]
    },
    {
        "question": r"Which of the following is described as a partial copy of a VM made at a particular moment?",
        "options": [
            r"Virtual instance",
            r"Differencing disk",
            r"Hypervisor",
            r"Checkpoint"
        ],
        "answer": [
            r"Checkpoint"
        ]
    },
    {
        "question": r"Which Windows Server 2012/R2 edition includes the license for one virtual instance of Windows Server 2012/R2?",
        "options": [
            r"Enterprise Edition",
            r"Standard Edition",
            r"Datacenter Edition",
            r"Essentials Edition"
        ],
        "answer": [
            r"Standard Edition"
        ]
    },
    {
        "question": r"What type of virtualization environment are you most likely to use for server virtualization in data centers? (Choose all that apply.)",
        "options": [
            r"Hosted virtualization",
            r"Type 2 hypervisor",
            r"Bare-metal virtualization",
            r"Type 1 hypervisor"
        ],
        "answer": [
            r"Bare-metal virtualization",
            r"Type 1 hypervisor"
        ]
    },
    {
        "question": r"You have just purchased a server with Windows Server 2012 R2 Datacenter Edition installed. The server has 4 GB RAM, a 200 GB hard disk, and an Intel 1.6 GHz Xeon processor with Intel-VT. You plan to install the Hyper-V server role on this server and run two Windows Server 2012 R2 VMs, each with a 2 GB RAM allocation. You have found that this server doesn’t work for this purpose, however. What should you do?",
        "options": [
            r"Install more RAM.",
            r"Install a bigger hard disk.",
            r"Install Standard Edition.",
            r"Upgrade the processor."
        ],
        "answer": [
            r"Install more RAM."
        ]
    },
    {
        "question": r"If you want to run two VMs, each running Windows Server 2012 R2 Standard Edition as the guest OS, on a Windows Server 2012 R2 Standard Edition server, how many Windows Server 2012 R2 licenses must you purchase?",
        "options": [
            r"1",
            r"2",
            r"3",
            r"None"
        ],
        "answer": [
            r"1"
        ]
    },
    {
        "question": r"A virtual switch with the host’s physical NIC bound to the Hyper-V Extensible Virtual Switch protocol is called which of the following?",
        "options": [
            r"External virtual switch",
            r"Private virtual switch",
            r"Hosted virtual switch",
            r"Internal virtual switch"
        ],
        "answer": [
            r"External virtual switch"
        ]
    },
    {
        "question": r"You created a VM running Windows Server 2012 R2 and some applications. You want to create a second VM quickly that has the same configuration options and installed applications as the first one. You plan to use this second VM on the same Hyper-V server as the first. You want good disk performance from both VMs. What should you do?",
        "options": [
            r"Create a VM with a differencing disk. Assign the first VM’s virtual disk as the parent disk; the first VM will continue to use its original virtual disk.",
            r"Export the first VM, and import it with the “Copy the virtual machine” option to create the second VM.",
            r"Create a VM. Create a checkpoint of the first VM. Copy and rename the checkpoint file and use it for the second VM’s virtual hard disk.",
            r"Export the first VM and import it using the “Register the virtual machine in place” option. Use the imported VM as the second virtual server."
        ],
        "answer": [
            r"Export the first VM, and import it with the “Copy the virtual machine” option to create the second VM."
        ]
    },
    {
        "question": r"You have an old server running Windows Server 2012 R2 that has had intermittent hardware failures in the past few months that cause the server to shut down. You haven’t been able to isolate the problem, but you suspect the hard disks are beginning to fail, and the server is no longer under warranty. You have been using a Hyper-V server for about a year, with two VMs running on it. This quad-core server has plenty of disk space and ample processing power and memory. Which of the following might be a good solution for the ailing server that requires the least amount of cost and administrative effort?",
        "options": [
            r"Purchase a new machine. Remove the hard disk from the old server, and install it in the new server.",
            r"Create a VM on your Hyper-V server. Remove the hard disk from the old machine, and install it in the Hyper-V server. Set the disk offline and use it as a pass-through disk for the new VM.",
            r"Create a VM on your Hyper-V server. On the old server, run a physical-to-virtual conversion. Use the resulting virtual hard disk file as the virtual disk for the new VM. Take the old server offline.",
            r"Create a VM on your Hyper-V server. Install Windows Server 2012 R2 as the guest OS. Carefully configure the guest OS to match the old server’s configuration, and take the old server offline."
        ],
        "answer": [
            r"Create a VM on your Hyper-V server. On the old server, run a physical-to-virtual conversion. Use the resulting virtual hard disk file as the virtual disk for the new VM. Take the old server offline."
        ]
    },
    {
        "question": r"You have three VMs that must communicate with one another and with the host computer but not be able to access the physical network directly. What type of virtual network should you create?",
        "options": [
            r"Private",
            r"Internal",
            r"Hosted",
            r"External"
        ],
        "answer": [
            r"Internal"
        ]
    },
    {
        "question": r"You’re installing a new VM in Hyper-V that requires excellent disk performance for the installed applications to perform well. The applications require a virtual disk of about 200 GB. The host has two drives: one used as the Windows system drive and the other as a data drive of 500 GB. It’s currently running a VM that uses a virtual disk stored on the host’s data drive. This VM requires little disk access, uses only 20 GB of the host’s data drive, and will max out at 40 GB. What type of disk should you use for the new VM you’re installing?",
        "options": [
            r"Differencing disk",
            r"Dynamically expanding disk",
            r"Pass-through disk",
            r"Fixed-size disk"
        ],
        "answer": [
            r"Fixed-size disk"
        ]
    },
    {
        "question": r"Your Hyper-V server has a single disk of 300 GB being used as the system disk and to host a dynamically expanding disk for a Windows Server 2012 R2 VM. The VM’s virtual disk has a maximum size of 200 GB and is currently 80 GB and growing. You have only about 30 GB free space on the host disk. You have noticed disk contention with the host OS, and the constant need for the virtual disk to expand is causing performance problems. You also have plans to install at least one more VM. You have installed a new 500 GB hard disk on the host and want to make sure the VM doesn’t contend for the host’s system disk, and the expansion process doesn’t hamper disk performance. What should you do?",
        "options": [
            r"Create a new fixed-size disk on the new drive. Use the Disk Management MMC on the VM to extend the current disk to the new fixed-size disk.",
            r"Shut down the VM. Convert the dynamically expanding disk to a fixed-size disk, being sure to place the fixed-size disk on the new host drive. Connect the VM to the fixed-size disk in place of the dynamically expanding disk. Delete the old virtual disk.",
            r"Shut down the VM. Create a new fixed-size disk on the new drive. Copy the contents of the dynamically expanding disk to the new fixed-size disk. Connect the VM to the fixed-size disk in place of the dynamically expanding disk. Delete the old virtual disk.",
            r"Create a new fixed-size disk on the new drive. Add the fixed-size disk to the VM as a new disk. On the VM, create a new volume on the new disk, and begin saving files to the new volume."
        ],
        "answer": [
            r"Shut down the VM. Create a new fixed-size disk on the new drive. Copy the contents of the dynamically expanding disk to the new fixed-size disk. Connect the VM to the fixed-size disk in place of the dynamically expanding disk. Delete the old virtual disk."
        ]
    },
    {
        "question": r"Your network has had long power outages that have caused Hyper-V servers to shut down after the UPS battery is drained. When power returns, the Hyper-V servers restart automatically, but the VMs don’t start. You need to make sure the VMs start when the host starts. What should you do?",
        "options": [
            r"Change the VMs’ BIOS settings.",
            r"Write a script on the host that starts the VMs automatically when the host starts.",
            r"Reinstall Integration Services.",
            r"Change the automatic start action setting on the VMs."
        ],
        "answer": [
            r"Change the automatic start action setting on the VMs."
        ]
    },
    {
        "question": r"You solved the problem with VMs not starting when the host restarts, but now you notice that VMs take a long time to start when the host starts. On some hosts, you have as many as six VMs. You also find that the VM running an application server can’t initialize correctly because the VM running DNS isn’t available immediately. What can you do to improve VMs’ startup times and solve the application server problem?",
        "options": [
            r"Set a virtual machine priority in Hyper-V’s Settings window.",
            r"Set a startup delay for each VM, making sure the delay for the DNS server is lower than the application server’s.",
            r"Change the BIOS settings of the DNS server to use the Quick Boot option.",
            r"Assign more virtual processors to the VMs you want to start faster."
        ],
        "answer": [
            r"Set a startup delay for each VM, making sure the delay for the DNS server is lower than the application server’s."
        ]
    },
    {
        "question": r"Checkpoints for your test VMs are taking up too much space on the host’s system disk. You have two test VMs running, each with one checkpoint to represent the baseline testing environment. You’re finished with your current testing and are ready for another round of testing, but you want to make sure your checkpoints are stored on another volume. What should you do?",
        "options": [
            r"In Hyper-V Manager, change the checkpoints’ path in the Settings window to point to the other volume; the checkpoints are moved automatically.",
            r"Use File Explorer to move the checkpoint files from their current location to the other volume.",
            r"Shut down the VMs. Apply the checkpoint to each VM, and delete all checkpoints in Hyper-V Manager. Change the path of the checkpoint files to the other volume, and create a new checkpoint for each VM.",
            r"In each VM’s settings, change the checkpoint path. Apply the checkpoint, and then create a new checkpoint for each VM. Delete the old checkpoints in File Explorer."
        ],
        "answer": [
            r"Shut down the VMs. Apply the checkpoint to each VM, and delete all checkpoints in Hyper-V Manager. Change the path of the checkpoint files to the other volume, and create a new checkpoint for each VM."
        ]
    },
    {
        "question": r"Which of the following is true about using differencing disks?",
        "options": [
            r"Checkpoints can be used with differencing disks, but performance is decreased.",
            r"The parent disk must not be changed.",
            r"The parent disk must always be connected to a running VM.",
            r"Differencing disks are very similar to fixed-size disks."
        ],
        "answer": [
            r"The parent disk must not be changed."
        ]
    },
    {
        "question": r"You have four checkpoints of a VM. You want to return the VM to its state when the second checkpoint was taken. Which checkpoint option should you use?",
        "options": [
            r"Apply",
            r"Save",
            r"Select",
            r"Revert"
        ],
        "answer": [
            r"Apply"
        ]
    },
    {
        "question": r"You’re working with a Windows Server 2003 VM in Hyper-V. Every time you click the mouse in the VM window, it’s captured, and you have to press Ctrl+Alt+left arrow to use the mouse on the host OS, which is getting annoying. What can you do to make using the VM easier?",
        "options": [
            r"Install a new mouse on the host system that supports Hyper-V.",
            r"Install Integration Services on the host computer.",
            r"Install Integration Services on the VM.",
            r"Install emulated mouse drivers on the VM."
        ],
        "answer": [
            r"Install Integration Services on the VM."
        ]
    },
    {
        "question": r"You want to run four VMs on a Hyper-V server. Two VMs need to be assigned 1 GB RAM, and two need to be assigned 1.5 GB RAM for optimal performance. How much RAM should be installed on the host computer?",
        "options": [
            r"512 MB",
            r"4 GB",
            r"5 GB",
            r"6 GB"
        ],
        "answer": [
            r"6 GB"
        ]
    },
    {
        "question": r"You want to run three VMs on a Hyper-V server. Two of the VMs should be assigned two virtual processors, and the other requires only one. The host should have at least four processor cores dedicated to it. What configuration should you use on the host?",
        "options": [
            r"A quad-core CPU",
            r"Two quad-core CPUs",
            r"Two dual-core CPUs",
            r"One quad-core and one dual-core CPU"
        ],
        "answer": [
            r"Two quad-core CPUs"
        ]
    },
    {
        "question": r"You have just installed a VM named VM5 running an application that requires the best possible network performance when communicating with resources on the physical LAN. The host has four NICs. One NIC is dedicated to the host computer, and the other two are bound to two virtual switches used by four other VMs on the system. One of the NICs is currently unused. What network configuration should you use that wouldn’t disturb the current VM’s network configuration?",
        "options": [
            r"Connect VM5 to an internal network, and run RRAS on the host server.",
            r"Connect the four existing VMs to a private network, create a NIC team on the host server, and bind the NIC team to a virtual switch for VM5 to use.",
            r"In Virtual Switch Manager, bind the unused NIC to an external virtual switch and enable SR-IOV. Connect VM5’s virtual network adapter to that virtual switch and enable SR-IOV on the virtual network adapter.",
            r"Create a NIC team in VM5, using all four NICs on the host. Turn on virtual network adapter sharing so that the NICs can be used for both the team and the other two virtual switches."
        ],
        "answer": [
            r"In Virtual Switch Manager, bind the unused NIC to an external virtual switch and enable SR-IOV. Connect VM5’s virtual network adapter to that virtual switch and enable SR-IOV on the virtual network adapter."
        ]
    },
    {
        "question": r"You created a VM and installed Windows Server 2008 R2 over the network, using PXE boot. When you start the VM, it doesn’t attempt to boot from the network. What should you do?",
        "options": [
            r"Install a legacy virtual network adapter.",
            r"Configure the VM as a generation 2 VM.",
            r"Install a synthetic virtual network adapter.",
            r"Enable PXE boot in the VM’s BIOS settings."
        ],
        "answer": [
            r"Install a legacy virtual network adapter."
        ]
    },
    {
        "question": r"You currently have four VMs running on a Hyper-V server. You find that VM2 sometimes monopolizes disk I/O. You want to limit the amount of disk resources VM2 can use so that the other VMs have satisfactory disk performance. What should you do?",
        "options": [
            r"Enable SR-IOV on VM2’s virtual hard disk.",
            r"Enable virtual hard disk sharing on VM2.",
            r"Configure VM2’s disk as a pass-through disk.",
            r"Enable storage QoS on VM2’s virtual hard disk."
        ],
        "answer": [
            r"Enable storage QoS on VM2’s virtual hard disk."
        ]
    },
    {
        "question": r"You currently have four VMs running on a Hyper-V server. You need to increase the amount of memory to VM4 so that you can install a new application. You’re running low on physical memory. You tried to allocate less memory to the other three VMs to free up memory, but after you did so, they wouldn’t start. What can you do that doesn’t involve installing additional physical memory on the host or changing the configuration of the guest OSs?",
        "options": [
            r"Enable Dynamic Memory on all the VMs, and set the startup memory higher than the minimum memory.",
            r"Configure resource metering on all four VMs.",
            r"Uninstall server roles on the guest OSs until you have enough free memory for VM4.",
            r"Enable memory QoS on the other three VMs and set a maximum IOPS for their memory use."
        ],
        "answer": [
            r"Enable Dynamic Memory on all the VMs, and set the startup memory higher than the minimum memory."
        ]
    },
    {
        "question": r"You’re using a VM with a Windows 8.1 Pro guest OS to run applications that you want isolated from the host computer and the LAN. However, you want to be able to print from the VM to the printer connected to your host and copy files between the host and guest OS. The VM is connected to a private virtual switch. What can you do?",
        "options": [
            r"Enable Enhanced Session mode in Hyper-V, and verify that Remote Desktop Services is running on the guest.",
            r"Create shares on the host and VM to transfer files back and forth, and install a printer driver on the guest OS.",
            r"Connect the VM running Windows 8.1 to an external virtual switch.",
            r"Install Integration Services on the Windows 8.1 guest OS and enable the device-sharing and file-sharing options."
        ],
        "answer": [
            r"Enable Enhanced Session mode in Hyper-V, and verify that Remote Desktop Services is running on the guest."
        ]
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exam Practice")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.configure(bg="#2e2e2e")  # Dark background color

        self.style = Style()
        self.style.configure("TButton", background="#555555", foreground="white", font=('Helvetica', 12))
        self.style.configure("TLabel", background="#2e2e2e", foreground="white", font=('Helvetica', 12))
        self.style.configure("TCheckbutton", background="#2e2e2e", foreground="white", font=('Helvetica', 12))
        self.style.configure("TRadiobutton", background="#2e2e2e", foreground="white", font=('Helvetica', 12))

        self.progress = tk.DoubleVar()
        self.progress_bar = Progressbar(root, maximum=100, variable=self.progress)
        self.progress_bar.pack(fill='x', pady=10)

        self.remaining_questions = questions.copy()
        self.current_question = None
        self.selected_option = []
        self.option_vars = []
        self.question_number = 0
        self.total_questions = len(questions)
        self.time_remaining = 90 * 60  # 1.5 hours in seconds

        self.timer_label = tk.Label(root, text="", font=('Helvetica', 12), bg="#2e2e2e", fg="white")
        self.timer_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", wraplength=700, justify="left", font=('Helvetica', 14), bg="#2e2e2e", fg="white")
        self.question_label.pack(pady=10)

        self.counter_label = tk.Label(root, text=f"Question {self.question_number + 1}/{self.total_questions}", font=('Helvetica', 12), bg="#2e2e2e", fg="white")
        self.counter_label.pack(pady=10)

        self.options_frame = tk.Frame(root, bg="#2e2e2e")
        self.options_frame.pack(pady=10, fill='x', expand=True)

        self.next_button = tk.Button(root, text="Submit", command=self.check_answer, bg="#555555", fg="white")
        self.next_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_selection, bg="#555555", fg="white")
        self.reset_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", fg="red", font=('Helvetica', 12), bg="#2e2e2e")
        self.result_label.pack(pady=10)

        self.update_timer()
        self.load_new_question()

    def update_timer(self):
        if self.time_remaining <= 0:
            messagebox.showinfo("Time's up", "The time for the quiz has ended.")
            self.root.quit()
        else:
            mins, secs = divmod(self.time_remaining, 60)
            self.timer_label.config(text=f"Time Remaining: {mins:02}:{secs:02}")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)

    def load_new_question(self):
        if not self.remaining_questions:
            self.result_label.config(text="All questions have been answered!", fg="blue")
            return

        self.current_question = random.choice(self.remaining_questions)
        self.remaining_questions.remove(self.current_question)
        self.question_label.config(text=self.current_question["question"])
        self.question_number += 1
        self.counter_label.config(text=f"Question {self.question_number}/{self.total_questions}")
        self.progress.set((self.question_number / self.total_questions) * 100)
        self.selected_option = []
        self.option_vars = []

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        options = self.current_question["options"]
        random.shuffle(options)

        if len(self.current_question["answer"]) == 1:
            self.option_vars.append(tk.StringVar(value="0"))
            for idx, option in enumerate(options, start=1):
                radio = tk.Radiobutton(self.options_frame, text=option, variable=self.option_vars[0], value=option, indicatoron=0, pady=5, wraplength=700, justify="left", command=lambda opt=option: self.update_single_selection(opt), bg="#2e2e2e", fg="white", selectcolor="#555555")
                radio.pack(anchor="w", fill='x', expand=True)
        else:
            for idx, option in enumerate(options, start=1):
                var = tk.StringVar(value="0")
                self.option_vars.append(var)
                chk = tk.Checkbutton(self.options_frame, text=option, variable=var, onvalue=option, offvalue="0", wraplength=700, justify="left", command=lambda v=var: self.update_multi_selection(v), bg="#2e2e2e", fg="white", selectcolor="#555555")
                chk.pack(anchor="w", fill='x', expand=True)

    def update_single_selection(self, option):
        self.selected_option = [option]

    def update_multi_selection(self, var):
        if var.get() != "0":
            if var.get() not in self.selected_option:
                self.selected_option.append(var.get())
        else:
            if var.get() in self.selected_option:
                self.selected_option.remove(var.get())

    def check_answer(self):
        if len(self.current_question["answer"]) == 1:
            if self.selected_option == self.current_question["answer"]:
                self.highlight_option(self.selected_option[0], "green")
                self.result_label.config(text="Correct!", fg="green")
                self.root.after(2000, self.load_new_question)
            else:
                self.highlight_option(self.selected_option[0], "red")
                self.result_label.config(text="Incorrect. Try again.", fg="red")
        else:
            selected_options = self.selected_option
            correct_answers = self.current_question["answer"]
            correct_count = sum([1 for opt in selected_options if opt in correct_answers])
            incorrect_count = sum([1 for opt in selected_options if opt not in correct_answers])

            for opt in selected_options:
                if opt in correct_answers:
                    self.highlight_option(opt, "green")
                else:
                    self.highlight_option(opt, "red")

            if correct_count == len(correct_answers) and incorrect_count == 0:
                self.result_label.config(text="Correct!", fg="green")
                self.root.after(2000, self.load_new_question)
            else:
                remaining_correct = len(correct_answers) - correct_count
                if remaining_correct == 0 and incorrect_count == 0:
                    self.result_label.config(text="Correct!", fg="green")
                    self.root.after(2000, self.load_new_question)
                else:
                    self.result_label.config(text=f"Some correct. Select {remaining_correct} more correct options.", fg="red")

    def reset_selection(self):
        for var in self.option_vars:
            var.set("0")
        self.selected_option = []
        self.result_label.config(text="")

    def highlight_option(self, option, color):
        for widget in self.options_frame.winfo_children():
            if widget.cget("text") == option:
                widget.config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()