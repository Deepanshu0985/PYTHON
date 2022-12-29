import pygal

worldmap = pygal.maps.world.World()

worldmap.title = 'Countries'

worldmap.add('Random Data',{
    'aq' : 10,
    'cd' : 30,
    'de' : 40,
    'eg' : 50,
    'ga' : 45,
    'hk' : 23,
    'in' : 70,
    'jp' : 54,
    'nz' : 41,
    'kz' : 32,
    'us' : 66
})

worldmap.render_to_file('abc.svg')
print("success")