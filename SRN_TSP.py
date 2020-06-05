import random
from turtle import *
import math
import copy


def student_details():
    # add variables to store student ID and username to be returned
    student_id = 15043461
    student_username = "Elias Mahamoud" 	
    return student_id, student_username


def generate_map(x_range, y_range, locations):
    # add code to create a list then use a for loop to create a random population for this list
    listOfCities = []
    for i in range(locations):
        listOfCities.append([])
    for i in range(locations):
        listOfCities[i].append(random.randint(-x_range, x_range))
        listOfCities[i].append(random.randint(-y_range, y_range))
    generated_map = listOfCities
    return generated_map


def print_map(speed, color, thickness, selected_map):
    print("printing map")

    # add code to use the turtle to draw the path between all destinations
    # the turtle should make use of the parameters provided: speed. color, etc...
    # you will need to use a loop in order to draw the path to all locations
    for j in range(len(selected_map) - 1):
        xpoint1 = selected_map[j][0]
        ypoint1 = selected_map[j][1]
        xpoint2 = selected_map[j + 1][0]
        ypoint2 = selected_map[j + 1][1]
        penup()
        goto(xpoint1, ypoint1)
        pendown()
        goto(xpoint2, ypoint2)
    done()


def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x,
                          destination_y - starting_y)  # calculates Euclidean distance (straight-line) distance between two points
    return distance


def calculate_path(selected_map):
    # you will need to setup a variable to store the total path distance
    # you will need to use a loop in order to calculate the distance of the locations individually
    # it would be wise to use make use of the calculate_distance function as you can reuse this
    # remember your need to calculate the path of all locations returning to the original location

    total_path = 0
    for i in range(len(selected_map) - 1):
        total_path = total_path + calculate_distance(selected_map[i][0], selected_map[i][1], selected_map[i + 1][0],
                                                     selected_map[i + 1][1])
    total_path = total_path + calculate_distance(selected_map[0][0], selected_map[0][1],
                                                 selected_map[len(selected_map) - 1][0],
                                                 selected_map[len(selected_map) - 1][1])
    distance = total_path

    return distance


#################################################################################################

def nearest_neighbour_algorithm(selected_map):
    temp_map = copy.deepcopy(selected_map)

    # you need to create an empty list for your optimised map

    optimised_map = []
    for i in range(len(selected_map)):
        optimised_map.append([])
    for i in range(len(selected_map)):
        optimised_map[i].append(0)  # x coordinate
        optimised_map[i].append(0)  # y coordinate

        # you need to add some variables to store establish the closest location
    index = 0
    xcoord = 0
    ycoord = 0
    minimum = float('inf')
    optimised_map[0][0] = selected_map[0][0]
    optimised_map[0][1] = selected_map[0][1]
    temp_map.pop(0)
    selectedCity = 0
    # NOTE: you can remove this line once function is implemented
    # you need to calculate the distance between the current path and the next potential location
    # it would be wise to use make use of the calculate_distance function

    for i in range(len(temp_map)):
        temp = i
        for j in range(len(temp_map)):
            distance = calculate_distance(optimised_map[selectedCity][0], optimised_map[selectedCity][1],
                                          temp_map[j][0], temp_map[j][1])
            if (distance < minimum):
                minimum = distance
                index = j
                xcoord = temp_map[j][0]
                ycoord = temp_map[j][1]
        minimum = float('inf')
        selectedCity = selectedCity + 1
        optimised_map[selectedCity][0] = xcoord
        optimised_map[selectedCity][1] = ycoord
        temp_map.pop(index)

        # you will need to write an if statement to establish if the current distance is lower than the stored
        # best distance, and if so set the best distance to the current location

        # the final step is to add the closest location to the optermised_map and remove from the temp_map
    optermised_map = copy.deepcopy(optimised_map)
    return optermised_map


#################################################################################################

def genetic_algorithm(selected_map, population, iterations, mutation_rate, elite_threshold):
    # this is the main genetic algorithm function and should make use of the inputs and call the sub functions in order to run

    # you will need to call the create_population function and store this in a list

    gene_pool = create_population(population, selected_map)
    # you will then need to use the iterator function and store the returned solution to best_solution

    best_solution = iterator(gene_pool, 500, 0.17, 0.2)

    return best_solution


def create_population(population, selected_map):
    # you need to create an empty list called gene_pool for the population
    # use a for loop and the provided inputs to create the population
    populationDetails = []
    for i in range(population):
        populationDetails.append([])

    # you will also need to randomise the individuals within the population
    for i in range(population):
        for j in selected_map:
            populationDetails[i].append(j)
        random.shuffle(populationDetails[i])

    gene_pool = populationDetails

    return gene_pool


def fitness_function(gene_pool, best_solution):
    # you need to find a way to rank the fitness of your population. one way you may consider doing this is with a ranked list

    # you will need to have correctly implemented the calculate_path function in order to rank the fitness of the population

    # you may consider using a loop to achieve this

    # your function must return a sorted gene pool that is sorted by fittest (shortest path to longest path

    # your function should also return the fittest individual in best_solution
    sorted_gene_pool = copy.deepcopy(gene_pool)
    for i in range(len(sorted_gene_pool)):
        for j in range(0, len(sorted_gene_pool) - 1 - i):
            if (calculate_path(sorted_gene_pool[j]) > calculate_path(sorted_gene_pool[j + 1])):
                temp = sorted_gene_pool[j]
                sorted_gene_pool[j] = sorted_gene_pool[j + 1]
                sorted_gene_pool[j + 1] = temp
    best_solution = sorted_gene_pool[0]
    return sorted_gene_pool, best_solution


def iterator(gene_pool, iterations, mutation_rate, elite_threshold):
    # you need to use the provided inputs to iterate (run) the algorithm for the specified iterations

    # you will need to use a for loop in order to achieve this

    # in order for this function to work all over parts of the algorithm must be complete

    # the function must return the best individual (best_solution) in the population
    best_solutions = []
    for i in range(iterations):
        new_gene_pool = mating_function(gene_pool, best_solutions, mutation_rate, elite_threshold)
    sorted_gene_pool = copy.deepcopy(new_gene_pool)
    for i in range(len(sorted_gene_pool)):
        for j in range(0, len(sorted_gene_pool) - 1 - i):
            if (calculate_path(sorted_gene_pool[j]) > calculate_path(sorted_gene_pool[j + 1])):
                temp = sorted_gene_pool[j]
                sorted_gene_pool[j] = sorted_gene_pool[j + 1]
                sorted_gene_pool[j + 1] = temp
    best_solution = sorted_gene_pool[0]
    return best_solution


def mating_function(gene_pool, best_solution, mutation_rate, elite_threshold):
    # you need to create a new list called new_gene_pool to store the newly created individuals from this function
    new_gene_pool = []
    # you will need to use a loop in order to perform the genetic crossover and mutations for each individual
    # in order for this function to work correctly you need to select the parent genes based to create the child

    # one of the top individuals based on the elite_threshold should be selected as one of the parents

    # once both parents have been chosen the breed function should be called using both of these parents
    eliteClass = []
    for i in range(int(elite_threshold * len(gene_pool)) + 1):
        eliteClass.append([])

    for i in range(len(eliteClass)):
        eliteClass[i] = gene_pool[i]

    for i in range(len(gene_pool)):
        if (i < len(eliteClass)):
            eliteParent = random.choice([j for j in eliteClass if j != eliteClass[i]])
        else:
            eliteParent = eliteClass[random.randint(0, len(eliteClass) - 1)]
        # this means the breed function must be working and returning a child

        child = breed(gene_pool[i], eliteParent)

        # once the breed function has returned a new individual this individual needs to be mutated
        # this means you need to implement the mutate function and it must return the mutated child

        mutated_child = mutate(child, mutation_rate)

        # the function must return a new generation of individuals in new_gene_pool

        new_gene_pool.append(mutated_child)

    return new_gene_pool


def breed(parent_1, parent_2):
    # you need to select random points in which to cut the genes of the parents and put them into the child

    # because the individual must contain all of the locations (this is a unique issue to the TSP) the gene selection is slightly more difficult

    # one suggested way is to selected portions of genetic data from one parent then fill in the remainder of locations from the other parent

    # the portion of genes selected should be random and you may want to use some for loops to achieve this

    # the function must return a child of the 2 parents containing all the locations in the original map

    randomCutStart = random.randint(0, len(parent_1) - 1)
    randomCutEnd = random.randint(0, len(parent_1) - 1)
    child = []
    index = 0
    for i in range(len(parent_1)):
        child.append([])
    for i in range(len(parent_1)):
        if (i >= min(randomCutStart, randomCutEnd) and i <= max(randomCutStart, randomCutEnd)):
            child[index] = parent_1[i]
            index = index + 1
    for i in range(len(parent_2)):
        if parent_2[i] not in child:
            child[index] = parent_2[i]
            index = index + 1

    return child


def mutate(child, mutation_rate):
    # this function must mutate the genes of the child based on the mutation rate provided

    # to achieve this you may want to use a for loop to go through the child

    # then use a random number with an if statement according the mutation rate

    # selected genes will then need to be swapped

    # the function must return a child containing all the locations in the original map but not as it originally arrived
    for i in range(len(child)):
        rand = random.random()
        if (rand < mutation_rate):
            swapCity = child[int(rand * len(child))]
            child[int(rand * len(child))] = child[i]
            child[i] = swapCity

    mutated_child = child
    return mutated_child



