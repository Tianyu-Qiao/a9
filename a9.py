ccf_venue_capacity = {"Venue1": 3, "Venue2": 2, "Venue3": 1}
test_venue_assignments = {"Examining Nighthawks": "Venue1","How Chicago got The Blues": "Venue1", "Anatomy of a Hubbard Street Dance": "Venue2","The History of the Lyric Opera House": "Venue3"}
sample_requests = [("S. Seaborn", ["Examining Nighthawks","How Chicago got The Blues"]), ("J. Bartlet", ["How Chicago got The Blues","The History of the Lyric Opera House"]),("J. Lyman", ["Examining Nighthawks","How Chicago got The Blues"]),("D. Moss", ["Anatomy of a Hubbard Street Dance","How Chicago got The Blues","Examining Nighthawks"]),("C. Young", ["Examining Nighthawks","How Chicago got The Blues"]),("T. Ziegler", ["How Chicago got The Blues", "Examining Nighthawks"]),("CJ. Cregg", ["Examining Nighthawks","How Chicago got The Blues"]),("L. McGarry", ["Examining Nighthawks","How Chicago got The Blues"]), ("A. Bartlet", ["Chicago's Skyline in Pictures","Anatomy of a Hubbard Street Dance", "How Chicago got The Blues"]),("M. Hooper", ["Chicago's Skyline in Pictures","Anatomy of a Hubbard Street Dance"]),("N. McNally", ["The History of the Lyric Opera House"])]
 
def allocate_seats(ccf_venue_capacity,test_venue_assignments, sample_requests):
 tem = {}
 for tva in test_venue_assignments:
  tem[tva] = ccf_venue_capacity[test_venue_assignments[tva]]
 
 tem2 = {}
 for sr in sample_requests:
  tem2[sr[0]] = 'Wait Listed'
  for item in sr[1]:
   if item in tem:
    if tem[item] > 0:
     tem2[sr[0]] = item
     tem[item] -= 1
     break
  
 print(tem2)
 
allocate_seats(ccf_venue_capacity,test_venue_assignments, sample_requests)