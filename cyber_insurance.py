# ============================================
#  AS | Attika Sufyan
#  Cybersecurity Student
#  GitHub: github.com/attikasufyan870-del
#  Course: EC-Council Cybersecurity
#  Topic: Basics of Cyber Insurance
#  Chapter: 3
#  Date: April 2026
# ============================================

def cyber_insurance_checker():
    print("=" * 50)
    print("  AS | Attika Sufyan — Cyber Insurance Tool")
    print("=" * 50)
    
    print("\n🛡️ Cyber Insurance Assessment System\n")
    
    # Business Type
    print("🏢 Business Type Select Karo:")
    print("1. Small Business")
    print("2. Medium Business")
    print("3. Large Enterprise")
    print("4. Individual")
    
    business = int(input("\nNumber select karo (1-4): "))
    
    # Data Type
    print("\n💾 Kaunsa Data Handle Karte Ho?")
    print("1. Customer Personal Data")
    print("2. Financial Data")
    print("3. Medical Data")
    print("4. General Data")
    
    data = int(input("Number select karo (1-4): "))
    
    # Previous Incidents
    print("\n⚠️ Pehle Koi Cyber Attack Hua?")
    print("1. Haan")
    print("2. Nahi")
    
    incident = int(input("Number select karo (1-2): "))
    
    # Calculate Risk Score
    score = business + data + incident
    
    print("\n" + "=" * 50)
    print("📊 Cyber Insurance Assessment Result:")
    print("=" * 50)
    
    # Insurance Recommendation
    if score <= 4:
        print("🟢 LOW RISK")
        print("💰 Basic Cyber Insurance Recommended")
        print("📋 Coverage: Data Breach, Malware")
        print("💵 Estimated Cost: Low Premium")
    elif score <= 7:
        print("🟡 MEDIUM RISK")
        print("💰 Standard Cyber Insurance Recommended")
        print("📋 Coverage: Data Breach, Ransomware, Business Loss")
        print("💵 Estimated Cost: Medium Premium")
    else:
        print("🔴 HIGH RISK")
        print("💰 Comprehensive Cyber Insurance Recommended")
        print("📋 Coverage: Full Protection Package")
        print("💵 Estimated Cost: High Premium")
    
    print("\n✅ Insurance Benefits:")
    print("1. Data breach cover karta hai")
    print("2. Legal fees pay karta hai")
    print("3. Business loss cover karta hai")
    print("4. Recovery costs deta hai")
    print("=" * 50)

# Program Start
cyber_insurance_checker()
