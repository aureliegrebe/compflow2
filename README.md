# compflow2

This library aims to be a one for one drop-in replacement of James Bind's now
archived [compflow]{https://github.com/jb753/compflow} library. The underlying
code is written in Rust, allowing similar performance to be obtained compared
to the original library.

## Why not fork the original repo?

The original library used a now depreciated build system that I never
succeeding in getting to work in newer versions of python. Plus, I already had
already wrote the underlying Rust library for other purposes.

## Documentation

For the moment, use the [documentation]{https://jamesbrind.uk/compflow-docs/}
for the original library. The API is the same, although I have not yet
implemented all features.

## Building

This project is built using [maturin]{https://www.maturin.rs/}
To build and install the python library, run the following command:
```
maturin develop -r
```

## To Do

- [x] Implement evaluations from Mach number
- [ ] Finish implementing inversion to Mach number
- [ ] Implement derivatives with respect to Mach number
- [ ] Implement lookup tables (maybe)
- [ ] Add parallel processing (maybe)



