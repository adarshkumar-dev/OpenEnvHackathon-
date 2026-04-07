# OpenEnv Customer Support Environment

## Overview
Simulates real-world customer support workflows including classification, response generation, and resolution.

## Tasks
- Easy: Ticket classification
- Medium: Response generation
- Hard: Full resolution workflow

## Action Space
- classify_ticket
- reply_to_customer
- close_ticket

## Run

```bash
docker build -t openenv .
docker run -p 7860:7860 openenv
