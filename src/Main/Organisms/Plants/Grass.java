package Main.Organisms.Plants;

import Main.Helper.Vector2D;
import java.awt.*;

public class Grass extends Plant {
    public static final double ENERGY_FACTOR = 6*scale;              //the factor that the eating of a Grass gives
    public static final double BASE_ENERGY_PROVIDED = 10*scale;        //base energy that eating a Grass gives
    public static final double GROWTH_INTERVAL = 10*scale;            //Interval at which Growth happens
    public static final double GROWTH = .001*scale;                     //Rate at which a Grass grows
    public static final double GROWTH_CHANCE = 5.;
    public static final double BASE_SIZE = 2;                   //Base size of a Grass
    public static final double HEALTH_REGENERATION = .001*scale;        //Amount that is regenerated at once
    public static final double MAX_HEALTH = 100*scale;                //Maximum health of a plant
    public static int totalAmount = 0;                          //total amount of Rabbits ever born
    public static double totalAvgAge = 0;                         //total avg age
    public Color col = new Color(150, 200, 20 ,125);


    //Constructor
    public Grass(){
        super();
        this.growthInterval = GROWTH_INTERVAL;
        this.expressGenes();

        totalAmount++;

        this.health = MAX_HEALTH;
    }

    /**
     * genes[0] = size
     */
    @Override
    public void expressGenes() {
        this.transform.size = this.dna.genes[0]+BASE_SIZE;
    }

    //Behavior
    public void update(){
        //if the plant is damaged use energy to regenerate, else to grow
        if(this.health < MAX_HEALTH){
            this.health += HEALTH_REGENERATION;
        }else{
            this.growthTimer--;
            if(this.growthTimer <= 0 && Math.random() < GROWTH_CHANCE){
                this.grow();
                this.growthTimer = this.growthInterval;
            }
        }
        //this.transform.size = Vector2D.map(this.health, 0, MAX_HEALTH, 0, this.transform.size);
    }

    @Override
    public Plant reproduce() {
        return null;
    }

    @Override
    public void grow() {
        this.transform.size += GROWTH;
    }

    @Override
    public void paint(Graphics2D g) {
        assert !this.isDead() : "This is dead";

        this.col = new Color(150, 200, 20 ,55+(int)Vector2D.map(this.health,0,MAX_HEALTH,0,200));
        g.setColor(this.col);
        g.fillOval((int)(this.transform.location.x-this.transform.size/2),(int)(this.transform.location.y-this.transform.size/2),(int)this.transform.size,(int)this.transform.size);
    }
}