# Build Responsive Real-World Websites with HTML and CSS


## Quick Jump
- [HTML Fundamentals](#html-fundamentals)
- [CSS Fundamentals](#css-fundamentals)
- [CSS Layouts](#css-layouts)
- [Design](#design)
- [Components](#components)


## HTML Fundamentals

### What is HTML?
- Hypertext Markup language
- Used to structure and describe webpage contents
- Consists of elements of different types
- Browsers render HTML code as websites


### `<Element>` Structure

```html    
          Content of Element    
                  ↑      
                  |
                  |
<p>HTML is a markup language.... </p>
 |                                 |
 |                                 |
 |-> Opening tag                   |
                                   |
                                   |
                     Closing tag <-|
```

- Opening Tag: `<element-name>`
- Closing Tag: `</element-name>`
- Content: Text or child elements or no content


### What is semantic HTML means?
That curation elements have a meaning or a purpose attached to them.

[Go Back 🔝](#quick-jump)

## CSS Fundamentals

### What is CSS?
- **C**ascading **S**tyle **S**heets
- Describes visual style of the content written in HTML
- Consists of countless properties that develop the content, properties about font, text, spacing, layout and etc..


### How We Select & Style Elements
```css
                 Declaration Block
-----------------------------------------------------
|                                                   |
|   |-> Selector                                    |
|   |                                               |
|   |                                               |
|   h1 {                                            |
|           color: blue;                            |
|           text-align: center;                     |
|           font-size: 20px; -> style/declaration   |
|               |        |                          |
|               |        |                          |
|    Property <-|        |-> Value                  |
|   }                                               |
-----------------------------------------------------
```


### The RGB Model
- Every color can be represented by a combination of Red, Green and Blue.
- Each of the 3 base colors can take a value between `0` and `255`

![RGB](https://upload.wikimedia.org/wikipedia/commons/c/c7/The_three_primary_colors_of_RGB_Color_Model_%28Red%2C_Green%2C_Blue%29.png)


### Defining Colors in CSS
1. RGB/RGBA Notation
```css
rgb(0, 255, 255)

/* The same as rgb(...) but with transparency */
rgba(0, 255, 255, 0.3)
```

2. Hexadecimal Notation
- Instead using a scale from `0` to `255`
- `ff` equal to `255` but in hexadecimal
- Shorthand when all colors are identical pairs `#0ff`
- When colors in all channels are the same we get *grey color*


```css
#00ffff
 |  | |----------> Blue
 |  |----> Green
 -> Red
```


### Resolving conflict

> Selectors are sort by priority

1. ID Selector `#`
2. Class Selector `.`
3. Element Selector `<any>`
4. Universal Selector `*`


### The Box Model
- Content: Text, Images, etc...
- Border: A line around the element
- Padding: Invisible space around the content
- Margin: Space outside of the element
- Fill area: Area that gets filled with background
- Size can by specified by width and height

![the-box-model](https://www.csssolid.com/images/box-model/css-box-model.png)


## Element height and width calculation
- width: padding left and right + border left and right + width
- height: padding top and bottom + border top and bottom + height

##### Notice
- This is the default behavior but we can change it


## Block-level Elements
- Elements are formatted visually as blocks
- Elements occupy **100%** of parent element width
- Elements are stacked vertically by default
- The box-model applies as showed earlier

##### Notice
- Most of the elements has this default behavior applied to them `display: block;`


## Inline Elements
- Occupies only the needed space for its content
- Causes no line-break after or before the element
- Box model applies in a different way (height and width don't apply)
- Padding and margins are applied only horizontally (left & right)


## Inline-block Elements
- Looks like inline from the outside but behaves like block-level on the inside
- Occupies only content's space
- Causes no line-break
- Box-model applies as showed `display: inline-block;`



## Normal Flow VS. Absolute Positioning

### Normal Flow
1. Default positioning
2. Elements is in flow
3. Elements are simply laid out according to their order in the HTML

```css
element {
   display: relative;
}
```

### Absolute Positioning
1. Elements is removed from the normal flow
2. No impact on surrounding elements, might overlap them
3. We use `top`, `bottom`, `right` and `left` to offset the element (relatively positioned from container)

```css
element {
   display: absolute;
}
```


[Go Back 🔝](#quick-jump)


## CSS Layouts
[Go Back 🔝](#quick-jump)


## Design
[Go Back 🔝](#quick-jump)


## Components
[Go Back 🔝](#quick-jump)