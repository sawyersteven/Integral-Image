# Integral Image
Simple python class to create an integral image or partial sum table

### Usage
    from integral_image import IntegralImage
    ii = IntegralImage(table)
	
Where `table` is a 2d `array` populated with `ints`.


##### get(x, y)
Returns value of the cell at `x, y`.
All cells are counted from `0` starting at the `top-left` corner.


##### box_sum(x, y, w, h)
Retuns the sum of a box starting at `x, y` with width `w` and height `h`.
`x, y` indicates the `top-left` corner of the box.
