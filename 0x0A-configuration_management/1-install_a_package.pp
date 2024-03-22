# Puppet manifest to install Flask from pip3

# Ensure the Flask package is installed and at version 2.1.0
package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
