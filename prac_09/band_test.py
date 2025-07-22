from band import Band, Musician, Instrument

# Create instruments
washburn = Instrument("Washburn N4", 1990, 2499.95)
takamine = Instrument("Takamine acoustic", 1986, 1200.00)
mouradian_bass = Instrument("Mouradian CS-74 Bass", 2009, 1500.00)

# Create musicians
nuno = Musician("Nuno Bettencourt")
nuno.add_instrument(washburn)
nuno.add_instrument(takamine)

gary = Musician("Gary Cherone")

pat = Musician("Pat Badger")
pat.add_instrument(mouradian_bass)

kevin = Musician("Kevin Figueiredo")

# Create a band
band = Band("Extreme")
band.add_musician(nuno)
band.add_musician(gary)
band.add_musician(pat)
band.add_musician(kevin)

# Print band details
print(band)

# Simulate the band playing
band.play()
