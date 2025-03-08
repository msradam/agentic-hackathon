# AskStreets: Query and Visualizing Street Networks using OpenStreetMap, ArangoDB, and LangGraph
Author: Adam Munawar Rahman, March 2025

Using powerful libraries like OSMnx, we can retrieve street networks and feature datasets from OpenStreetMap and persist them as graph and collections in ArangoDB. Then, with a  ReACT agent model, feed natural language queries to LLMs to execute complex lookups, run GPU backed graph algorithms, and visualize geospatial coordinates - all to enable streamlined insights into the network properties of the geographic area we are analyzing.

## Inspiration
During my internship at UNICEF Innovation in NYC, I used OpenStreetMap and NetworkX to calculate distances between schools and health facilities using country street networks. By writing code to execute graph algorithms, I was able to generate data to address a real-world issue.

I would like to extend this capability towards a more general use-case - if you're a city planner, business owner, or architect, you may also wish to ask questions about street networks but lack the ability to write lengthy algorithms. This is where AskStreets comes in - by providing the ability to translate natural language queries into street network analysis.

## What it does
AskStreets currently exists as a proof-of-concept within a Jupyter Notebook. It currently invokes a LangGraph ReAct agent to call multiple tools that can geocode, generate AQL, generate and execute OSMnx/NetworkX code, and visualize points on a Folium map.

By passing a query to the `query_street_network` function, it will invoke the ReAct agent to run these tools to interpret and provide a natural language response or map visualization for the specific question.

## How we built it
I used OSMnx to download street network graphs and geographic features for certain locations, prepared this data to load into ArangoDB, then wrote the LLM-based tools for the ReAct agent. 

## Challenges we ran into
Prompt engineering was a large aspect of this project, I needed to revise the prompts per tool multiple times as I continously tested and analyzed the output of the ReAct agent, so that I could provide the AI models with more context to properly interpret the user queries and assemble the correct code. Modifying the tools to properly interact with each other and work in tandem to generate the correct intermediate output for each to use was also a challenge.

## Accomplishments that we're proud of
I particularly enjoyed seeing the outcome of these tools, being able to correctly interpret user queries about street networks and correctly identifying the street network attributes to filter or run algorithms on.

## What we learned
I learned how to work with the LangChain and LangGraph libraries, how to invoke LLMs and prompt engineer to answer specific questions, and how to prepare OSMnx data to load into ArangoDB. 

## What's next for AskStreets: Querying and Visualizing Street Networks
Working with geospatial data has so much potential! In the submission notebook, I demonstrate at the end how health facility data can be overlaid with the graph and features data so that it can also be queried by AQL. By overlaying and combining different data sets, this has the potential to answer many different types of the queries.

The AI tools can also be enhanced to be more precise, for example, different models can be deployed for each tool for their particular usecase. More tools can also be written - for example, to pull in more data from OpenStreetMap if necessary - or the visualization tool can be updated to draw paths between points.
