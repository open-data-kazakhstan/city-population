from datapackage import Package

# Create a new package
package = Package(base_path='C:/Users/polat/Desktop/city-population/data')
package.infer('city_population.csv')

# Save the package to 'datapackage.json'
package.save('../datapackage.json')
