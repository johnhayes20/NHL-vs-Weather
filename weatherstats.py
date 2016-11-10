import urllib
import sqlite3
import re

begin = raw_input ('Press \'Enter\' to gather weather data based on the home city of NHL games in the past 10 years.')

#alphabetically ordered by name of home city
Cityurl = ['https://www.wunderground.com/history/airport/KFUL/2016/11/3/DailyHistory.html?req_city=Anaheim&req_state=CA&req_statename=California&reqdb.zip=92801&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KBOS/2016/11/3/DailyHistory.html?req_city=Boston&req_state=MA&req_statename=Massachusetts&reqdb.zip=02108&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KJRB/2016/11/3/DailyHistory.html?req_city=Brooklyn&req_state=NY&req_statename=New+York&reqdb.zip=11201&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KBUF/2016/11/3/DailyHistory.html?req_city=Buffalo&req_state=NY&req_statename=New+York&reqdb.zip=14201&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/CYYC/2016/11/3/DailyHistory.html?req_city=Calgary&req_state=AB&req_statename=Alberta&reqdb.zip=00000&reqdb.magic=2&reqdb.wmo=71877',
'https://www.wunderground.com/history/airport/KORD/2016/11/3/DailyHistory.html?req_city=Chicago&req_state=IL&req_statename=Illinois&reqdb.zip=60290&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KOSU/2016/11/3/DailyHistory.html?req_city=Columbus&req_state=OH&req_statename=Ohio&reqdb.zip=43085&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KDAL/2016/11/3/DailyHistory.html?req_city=Dallas&req_state=TX&req_statename=Texas&reqdb.zip=75201&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KBKF/2016/11/3/DailyHistory.html?req_city=Denver&req_state=CO&req_statename=Colorado&reqdb.zip=80201&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KDET/2016/11/3/DailyHistory.html?req_city=Detroit&req_state=MI&req_statename=Michigan&reqdb.zip=48201&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/CYXD/2016/11/3/DailyHistory.html?req_city=Edmonton&req_state=AB&req_statename=Alberta&reqdb.zip=00000&reqdb.magic=2&reqdb.wmo=71157',
'https://www.wunderground.com/history/airport/KGEU/2016/11/3/DailyHistory.html?req_city=Glendale&req_state=AZ&req_statename=Arizona&reqdb.zip=85301&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KCQT/2016/11/3/DailyHistory.html?req_city=Los+Angeles&req_state=CA&req_statename=California&reqdb.zip=90001&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/CYUL/2016/11/3/DailyHistory.html?req_city=Montreal&req_state=QC&req_statename=Quebec&reqdb.zip=00000&reqdb.magic=2&reqdb.wmo=71627',
'https://www.wunderground.com/history/airport/KBNA/2016/11/3/DailyHistory.html?req_city=Nashville&req_state=TN&req_statename=Tennessee&reqdb.zip=37201&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KNYC/2016/11/3/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&reqdb.zip=10001&reqdb.magic=11&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KEWR/2016/11/3/DailyHistory.html?req_city=Newark&req_state=NJ&req_statename=New+Jersey&reqdb.zip=07101&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/CYOW/2016/11/3/DailyHistory.html?req_city=Ottawa&req_state=ON&req_statename=Ontario&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=71628',
'https://www.wunderground.com/history/airport/KPHL/2016/11/3/DailyHistory.html?req_city=Philadelphia&req_state=PA&req_statename=Pennsylvania&reqdb.zip=19019&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KAGC/2016/11/3/DailyHistory.html?req_city=Pittsburgh&req_state=PA&req_statename=Pennsylvania&reqdb.zip=15201&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KRDU/2016/11/3/DailyHistory.html?req_city=Raleigh&req_state=NC&req_statename=North+Carolina&reqdb.zip=27601&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KSTP/2016/11/3/DailyHistory.html?req_city=Saint+Paul&req_state=MN&req_statename=Minnesota&reqdb.zip=55101&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KSJC/2016/11/3/DailyHistory.html?req_city=San+Jose&req_state=CA&req_statename=California&reqdb.zip=95101&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KCPS/2016/11/3/DailyHistory.html?req_city=Saint+Louis&req_state=MO&req_statename=Missouri&reqdb.zip=63101&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KFXE/2016/11/3/DailyHistory.html?req_city=Sunrise&req_state=FL&req_statename=Florida&reqdb.zip=33323&reqdb.magic=2&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/KTPF/2016/11/3/DailyHistory.html?req_city=Tampa&req_state=FL&req_statename=Florida&reqdb.zip=33601&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/CYKZ/2016/11/3/DailyHistory.html?req_city=Toronto&req_state=ON&req_statename=Ontario&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=71639',
'https://www.wunderground.com/history/airport/CYVR/2016/11/3/DailyHistory.html?req_city=Vancouver&req_state=BC&req_statename=British+Columbia&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=71892',
'https://www.wunderground.com/history/airport/KDCA/2016/11/3/DailyHistory.html?req_city=Washington&req_state=DC&req_statename=District+of+Columbia&reqdb.zip=20001&reqdb.magic=1&reqdb.wmo=99999',
'https://www.wunderground.com/history/airport/CYWG/2016/11/3/DailyHistory.html?req_city=Winnipeg&req_state=MB&req_statename=Manitoba&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=71852'
]

#alphbetically ordered by name of home city
City = ['Anaheim, California', 'Boston, Massachusetts', 'Brooklyn, New York', 'Buffalo, New York', 
'Calgary, Alberta', 'Chicago, Illinois', 'Columbus, Ohio', 'Dallas, Texas', 'Denver, Colorado', 
'Detroit, Michigan', 'Edmonton, Alberta', 'Glendale, Arizona', 'Los Angeles, California', 
'Montreal, Quebec', 'Nashville, Tennessee', 'New York City, New York', 'Newark, New Jersey', 
'Ottawa, Ontario', 'Philadelphia, Pennsylvania', 'Pittsburgh, Pennsylvania', 'Raleigh, North Carolina', 
'Saint Paul, Minnesota', 'San Jose, California', 'St. Louis, Missouri', 'Sunrise, Florida', 
'Tampa, Florida', 'Toronto, Ontario', 'Vancouver, British Columbia', 'Washington, D.C.', 'Winnipeg, Manitoba']

#alphabetically ordered by name of home city
TeamName = ['Anaheim Ducks', 'Boston Bruins', 'New York Islanders', 'Buffalo Sabres', 'Calgary Flames',
'Chicago Blackhawks', 'Columbus Blue Jackets', 'Dallas Stars', 'Colorado Avalanche', 'Detroit Red Wings',
'Edmonton Oilers', 'Arizona Coyotes', 'Los Angeles Kings', 'Montreal Canadiens', 'Nashville Predators',
'New York Rangers', 'New Jersey Devils', 'Ottawa Senators', 'Philadelphia Flyers', 'Pittsburgh Penguins',
'Carolina Hurricanes', 'Minnesota Wild', 'San Jose Sharks', 'St. Louis Blues', 'Florida Panthers',
'Tampa Bay Lightning', 'Toronto Maple Leafs', 'Vancouver Canucks', 'Washington Capitals', 'Winnipeg Jets']

#alphabetically ordered by name of home city
TeamAbrev = ['ANA', 'BOS', 'NYI', 'BUF', 'CGY', 'CHI', 'CBJ', 'DAL', 'COL', 'DET', 'EDM', 'ARI', 'LAK',
'MTL', 'NSH', 'NYR', 'NJD', 'OTT', 'PHI', 'PIT', 'CAR', 'MIN', 'SJS', 'STL', 'FLA', 'TBL', 'TOR', 'VAN',
'WSH', 'WPG']

#establishes cursor to write to db
conn = sqlite3.connect('HockeyWeatherdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''

CREATE TABLE IF NOT EXISTS HockeyWeather (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	Home     TEXT,
	Opponent   TEXT,
	MeanTemp	INTEGER,
	Date	TEXT,
	GF INTEGER,
	GA INTEGER
)
''')

#Establishes the location in the databse where the program will start writing if data has already been written
#This allows for the program to be stopped and restarted
startpoint = 0
try:
	for row in cur.execute('SELECT * FROM HockeyWeather ORDER BY id'):
		startpoint = startpoint + 1
except:
	startpoint=0
print startpoint

#Allteams10year.txt contains all of the box scores for NHL games in the past 10 years
fname = 'Allteams10year.txt'
handle = open(fname)

for iter in range(len(TeamName)):
	handle = open(fname)
	for line in handle:
		if line.startswith(TeamName[iter]):
			if startpoint>0:
				startpoint = startpoint - 1
				print startpoint
				continue
			url = Cityurl[iter]
			item = re.findall('[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]', line)
			stats = line.split()
			#Team, Game, Opp Team, GP, W, L, T, OT, P, GF, GA, SF, SA, PPG, PP Opp, PP%, TS, PPGA, PK%, FOW, FOL, FOW%
			#acquire stats from the "spreadsheet" starting from the end because team name length varies. there are 0-21 columns 
			GF = stats[-13]
			GA = stats[-12]
			OppTeam = stats[-20]
			#this creates the url to retrieve the mean temp given a date from Allteams10year.txt
			date = item[0]
			urlbegin = url[0:50]
			urlend = url[59:]
			urlfinal = urlbegin + date + urlend
			#accesses weatherunderground
			uh = urllib.urlopen(urlfinal)
			data = uh.read()
			weather = re.findall('Mean Temperature.*\n.*\n.*[0-9]+', data)
			#this accomodates for temps ranging from -99 to 999 degrees F
			try:
				meantemp = int(weather[0][-3:])
			except:
				try:
					meantemp = int(weather[0][-2:])
				except:
					try:
						meantemp = int(weather[0][-1:])
					except:
						pass
				
			print TeamName[iter], 'vs', OppTeam, 'mean temp: ', meantemp, 'date: ', date, 'Goals For: ', GF, 'Goals Against', GA
			
			cur.execute('''INSERT OR IGNORE INTO HockeyWeather 
				(Home, Opponent, MeanTemp, Date, GF, GA) VALUES ( ?, ?, ?, ?, ?, ? )''',
				(TeamAbrev[iter], OppTeam, meantemp, date, GF, GA) )
			cur.execute('SELECT id FROM HockeyWeather WHERE Home = ? ', (TeamAbrev[iter], ))
			user_id = cur.fetchone()[0]
			
			conn.commit()
			
