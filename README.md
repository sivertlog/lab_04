# Lab 04: *Jack Strikes Back*

### Encapsulation

*Encapsulation* greatly reduced complexity of this project.
Writing all of the components together would have been a jumbled mess,
but individually they are very manageable. Error checking is also 
much easier with this approach. We can test each function as we write it, 
and we know the errors associated with that function are isolated to 
either the function or the function call.

### Generalization

*Generalization* made the functions much more usable. With this 
approach the jack-o'-lanterns and their components scale in size making 
the design of the scene very easy to adjust. If we want to add 
another jack-o'-lantern all we need to do is call a function.