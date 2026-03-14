# Subnet Examples for Project

This document explains the **subnetting concepts applied** in the network design.

---

## 1. Base Network
- Network: 192.168.10.0/24  
- Total IPs: 256 (0-255)  
- Goal: Divide into 3 subnets for HR, Finance, IT

---

## 2. Subnetting Process

### Step 1: Determine subnet size
- Each department requires 62 usable IPs → Use **/26 subnet mask (255.255.255.192)**  
- Formula: `2^(32 - subnet bits) - 2` = usable hosts  
  - 32-26 = 6 bits for host  
  - `2^6 - 2 = 62` hosts per subnet

### Step 2: Assign subnets
| Department | Network Address | Broadcast | Usable IPs       |
|------------|----------------|-----------|----------------|
| HR         | 192.168.10.0   | 192.168.10.63  | 192.168.10.1 – 192.168.10.62 |
| Finance    | 192.168.10.64  | 192.168.10.127 | 192.168.10.65 – 192.168.10.126 |
| IT         | 192.168.10.128 | 192.168.10.191 | 192.168.10.129 – 192.168.10.190 |

---

## 3. Example Calculations

### HR Department
- Network: 192.168.10.0/26  
- Subnet mask: 255.255.255.192  
- Gateway: 192.168.10.1  
- Usable IPs: 192.168.10.1 → 192.168.10.62  

### Finance Department
- Network: 192.168.10.64/26  
- Gateway: 192.168.10.65  
- Usable IPs: 192.168.10.65 → 192.168.10.126  

### IT Department
- Network: 192.168.10.128/26  
- Gateway: 192.168.10.129  
- Usable IPs: 192.168.10.129 → 192.168.10.190  

---

## 4. Summary
- **Subnet mask /26** ensures 62 hosts per department.  
- Each subnet has a unique **network, broadcast, and gateway**.  
- Proper subnetting prevents IP conflicts and ensures smooth communication.  
