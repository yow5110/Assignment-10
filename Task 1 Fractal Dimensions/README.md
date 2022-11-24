# Week 13 Task 1

In class we demonstrated a general way to calculate the fractal dimension of a shape. For our typical fractal "dendritic-shaped" pattern formed in diffusion limited aggregation, the expected fractal dimension is between 1 and 2. To be more precise - 1.7. 

There is a simpler way to show this. Using your DLA code from exam #3, calculate the number of particles n within a given radius r, as a function of r (see "sample radius.png"). If the shape is fully two dimensional (e.g. a circular disk), then n should scale as pi*r**2. If the shape is one dimensional (e.g. a bar or line shape), then n should scale as r. We can therefore make a generalized statement that for an arbitrary shape, n scales as r**(the dimension of the shape D). 

Calculate n for a range of r values. Since n = C*r**D (where C is some constant), log(n) = log(C) + D*log(r). So if we plot log(n) versus log(r), the slope will be D. Draw several lines with slopes ranging from 1.5 to 2 and show that D is around 1.7. A quick example figure "sample log-log plot.png" is attached showing slopes of 1.6, 1.7 and 1.8. 

*If you know how to do linear fits that's fine too. But that's not required.