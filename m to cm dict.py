m_cm = {x: x *100 for x in range(1,11)}
#print(m_cm)
temp = m_cm.values()
#print(temp)
cm_m = {x: x /100 for x in temp}

print("Mtrs to Cms: ", m_cm)
print()
print("Cms to Mtrs: ", cm_m)
