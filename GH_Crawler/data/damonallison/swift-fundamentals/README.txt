# Swift

This repo contains Swift sample code (unit tests). Run the tests (`Cmd-U`) and
look in the `Documentation` folder for more info.


> "Swift is the first industrial-quality systems programming language that is as
> expressive and enjoyable as a scripting language." - Apple

> "The syntax and standard library have been designed based on the guiding
> principle that the obvious way to write your code should also perform the
> best." - Apple

> "Its combination of safety and speed make Swift an excellent choice for
> everything from “Hello, world!” to an entire operating system." - Apple


Swift is a statically typed, compiled lanaguage with a functional / dynamic
language feel. It's fast, safe, and modern. Swift follows `go` in continuing the
trend of making safe, statically typed language that feels like a dynamic
scripting language.


## Swift Links

* [swift.org](https://swift.org) - Swift's home.
* [forums.swift.org](https://forums.swift.org) - All development forums.
* [Documentation](https://swift.org/documentation) - Documentation, including
  `The Swift Programming Language` book.
* [Chris Lattner's Homepage](http://www.nondot.org/sabre/): Chris started swift
  as well as the vast majority of the modern Apple toolchain, including LLVM and
  the compiler infrastructure.

## Swift Overview

> "It's designed to scale from "hello, world" to an entire operating system" - The Swift Programming Language

The main themes of swift are `safe` and `modern`. Swift is strongly typed, but
really feels like a scripting language.

### Safe

* Strongly Typed
  * Explicit type casting required.
  * Generics.
  * Type inference.

* Optionals
  * One true "empty" (sentinal?) value to rule them all (nil, NSNotFound, 0, etc..)
  * Any type can be `optional`, even "primitives" like Int.

* Object initialization : all properties must have a value or the object fails initialization.
    * Much better than Objective-C's `if (self = [super init])` initializer.
    * Also much safer and strict. Objective-C was more confusing, especially around when you could use `self`.

* Access control.
  * Safe by default. 

* Fast memory management.
  * Pointers are hidden by default.


### Modern

* No header files.
* Functions are first class.
* String interpolation.
* Tuples allow for simple data structures and multiple return values.
* ivars are removed. You cannot define or access a property's ivar directly. Much less error prone.
* var / let : no need for non-mutable and mutable versions of the same classes (e.g. NSString, NSMutableString)
* Pattern matching and variable capture in `switch`.
* Flexible `enums` and `structs`.

* Defer
  * A better way to clean up resources.

* Error handling
  * Clean, performant in that it doesn't unwind the stack.

* Conditionals
  * Conditionals `must be` boolean expressions.
  * Switch automatically `break`s.

#### Evolution of Objective-C : "Swift is `Objective-C without the C`"

Objective-C and the underlying compiler infrastructure has been updated over the
years which "paved the way" for swift.

* Interoperable with Objective-C. 
  * Swift was built to interoperate with Objective-C. Apple could not simply
    update the entire cocoa library, therefore swift bridges with Objective-C
    nicely.

* Based on ARC.
  * Swift is still subject to retain cycles. Apple provides "capture lists" to
    allow developers to specify capture semantics.



### Dislikes

* There is no code-formatter (`go-fmt`).
  * No style consistency between projects.
  * Requires each team to have bike shedding "style wars".

* Memory management / retain cycles.
  * While memory is *mostly* managed for you, there are still edge cases which require running leak detection before shipping.



## Swift Language

### Access Control

* All members `internal` by default. `public` needs to be explicit.
* If your type is `private`, all members will be private by default.
* The access level of a tuple type is the most restrictive of it's members.
* The access level for a function is the most restrictive access level of it's parameter and return types.

#### Open

* Open grants anyone inside or outside the module the ability to subclass the `open` class.
  * Marking a class as `open` says:

    > I've considered the impact of code from other modules subclassing this class.

  * Applies to classes and class members only.
  * Allows classes to be subclassed from any module.

* **Only use open when you specifically want to allow external modules the ability to subclass.**
* If you just want to expose the function publicly, without the ability to override, use `public`.

### Public

* `public`
  * The public API for the framework.
  * Swift requires you to mark public API as `public` to force you to think
    about what you are doing.

* `@testable` allows a unit test target to access any internal entity within the
  module being imported. You do *not* need to make a member public just to test
  it.

* You can specify the access level of the getter and setter for a property:

```
	public private(set) var numberOfEdits = 0
```

-------

### Attributes (declaration modifiers)

* `dynamic` : use dynamic dispatch for this member. Implies `objc`.
* `objc` : make the declaration available to Objective-C.


## Tools

* [Jazzy](https://github.com/Realm/jazzy) : HTML Documentation generator for swift and objc. Outputs documentation files in HTML which mirror Apple's documentation look and feel.
