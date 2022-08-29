# advent-of-code

- [advent-of-code](#advent-of-code)
  - [Summary](#summary)
  - [Utilities](#utilities)
    - [Download Input Files](#download-input-files)
    - [Run Solution](#run-solution)

## Summary

[Advent of Code](https://adventofcode.com/) is a series of programming puzzles published yearly as an advent calendar.
This repository contains solutions to some problems, as well as a small project set up to help download and run the solutions.

## Utilities

### Download Input Files

To download the input files and prepare a solution template for a given year and day, run the command

`poetry run python aoc.py prepare {year} {day}`

The problem input and solution template will be placed in the folder `solutions/{year}/{day}`

### Run Solution

To run the solution for a given year and day, run the command

`poetry run python aoc.py run {year} {day}`
