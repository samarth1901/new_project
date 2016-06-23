PLAYER = 'PL'
OWNER = 'OW'
PROFILE_TYPE_CHOICES = (
	(PLAYER, 'Player'),
	(OWNER, 'Owner'),
)


PUNE = 'PUN'
MUMBAI = 'BOM'
DELHI = 'DEL'
BANGALORE = 'BAN'
CHENNAI = 'CHE'
PLACE_CHOICES = (
	(PUNE,'Pune'),
	(MUMBAI,'Mumbai'),
	(DELHI,'Delhi'),
	(BANGALORE,'Bangalore'),
	(CHENNAI,'Chennai'),
)

DOY = ('1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979','1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010',)

PLAYER = 'P'
OWNER = 'O'
GROUND = 'G'
SEARCH_CHOICES = (
	(PLAYER,'Player'),
	(OWNER,'Turf Owners'),
	(GROUND,'Ground/Turfs'),
)

AMETUER = 'Ametuer'
SEMI_PRO = 'Semi Pro'
PRO = 'Professional'
WORLD_CLASS = 'World Class'
EXPERTISE_CHOICES = (
	(AMETUER,'Ametuer'),
	(SEMI_PRO,'Semi Pro'),
	(PRO,'Professional'),
	(WORLD_CLASS,'World Class'),
)