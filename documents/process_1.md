## Process

0.5 vol of alumina, 0.5 vol water, 3% wt gelatin. Cured overnight in the fridge, though I think this was too long. Then I baked it at 70c for a few hours. The alumina layer seemed to settle to the bottom, forming a dense layer; a layer of water floated above. I'm not sure why.

## Results





If you’re anything like me, sometimes you get a hankering for some homemade vacuum feedthroughs.

Vacuum, of course, requ

https://outgassing.nasa.gov/

http://esmat.esa.int/Databases/databases.html

If you want to  LIGO and CERN

 and you’re tired of those bland, lifeless Delrin insulators, what with their atrocious 0.43% TML [nasa page overlay]. And you definitely don’t want to go to the store and pick up some insulators

You can make a ceramic

When fully vitrified, both alumina and electrical porcelain are vacuum compatible.





Bake until golden brown.

Of course, I wanted to do this with what I had on hand.

> 

So what you really want is some kind of organic binder that's both sufficiently low viscosity to flow into the mold when mixed with your desired ceramic powder, sufficiently strong when "cured" to be cleanly extracted from the mold, usable at sufficiently low percentages so that you don't get porosity or shrinkage after vaporization, and something that burns off cleanly when firing.

This shares some similarities with baking:

I mean, don’t let me near a stove.

Some examples are alginate with calcium iodate, fancy water-soluble epoxies, white PVA school glue, egg white. Okay, perhaps not egg white.

<https://s3.amazonaws.com/academia.edu.documents/46243057/j.1551-2916.2008.02534.x20160605-9566-1bhuice.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1541877772&Signature=0NrGbqgG1A8M3%2B9ZoBmqZkjXGmo%3D&response-content-disposition=inline%3B%20filename%3DCross-linked_Polyvinyl_Alcohol_as_a_Bind.pdf>

"Fabrication of alumina green body through gelcasting

process using alginate"

My favorite, however, is gelatine.



Porcelain slip generally relies on the plaster absorbing moisture from the material. In my case, the green would be far too thick to absorb the water anyhow. Porcelain shrunk significantly when drying at 85c. The green was almost perfect, except for the shrinkage. I bet a closed mold with a sprue and reservoir would fix that. However, Alumina has some properties that I need for other sections of the system, so I figured I'd drop porcelain for now and focus on that.

Glass is also sometimes acceptable. However, some parts of my chamber will have to withstand somewhere around 1600c, so having the ability to make ceramic parts would really be invaluable.

You can press and sinter alumina pretty easily. There's a number of sub-techniques here, with wet or dry die pressing, hot or cold isostatic, etc. The main limitation here is that you need to make press dies out of quite a hard material. You might be able to get away with aluminum for a few shots, but usually these dies are made of some sort of hardened steel. My dirt-cheap 6040 CNC is not going to cut it, what with its 50 thou chatter and whatnot.



Simple freeze-casting is possible, where an aqueous solution of alumina is frozen; however, crystal formation leads to high porosity and defects.

<>

As you might imagine, porosity is not particularly good in vacuum applications, as you'll get virtual leaks and contamination.

<https://www.osti.gov/servlets/purl/86933>

Alumina Casting Based on Gelation of Gelatine

At the end of the day, these alumina pieces actually have a tensile strength higher than that of 6061 aluminum.

0.5 vol of alumina, 0.5 vol water, 3% wt gelatin. Cured overnight in the fridge, though I think this was too long. Then I baked it at 70c for a few hours. The alumina layer seemed to settle to the bottom, forming a dense layer; a layer of water floated above. I'm not sure why.

<https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1151-2916.1996.tb08006.x>

Gel-cast process 1



The paper details a 3% shrinkage during drying, and a 17% shrinkage during sintering.

This is way, way too liquid. I need a much higher alumina content.

The solution cracked in the mold significantly - I omitted the fridge step. I think the drying needs to be done a little slower. Some solution left in the mixing cup became an almost perfect texture.

I think the reason for the cracking is pretty simple: the corner radii on the mounting flanges dried far faster than the rest of the material.

Z shrinkage was pretty terrible. From a 5mm high fill in the mold, only 2.8mm remained - 44% shrink. I guess that makes perfect sense, given a 50% solids loading. My current hypothesis is that my aggressive drying procedure evaporates the gelatine, producing a heavily green part.

Green strength was pretty good; if the other issues hadn’t presented themselves I think these would have been fine parts.

Porosity was okay.



I should try using a delrin insert as the middle piece, and removing the mounting flanges.

I can use a seperate 3d printed piece for the back plate and all that stuff.

Use gelatin as the mold itself somehow? Nah, then it’ll melt at the same time as the cast part.

PARAFFIN WAX MOLD. Melt it away after drying. Temperature of 50-60c or so. Perfect. Or perhaps glue stick glue?

There was a lot of foam produced on the surface of the alumina slurry while mixing. I think it might be a good idea to add the gelatine after stirring in the alumina.

It might be possible to use two different types of wax.

I really should pick up some white glue. It would be much easier to work with a harder, higher-temperature green.

<https://wfs.swst.org/index.php/wfs/article/viewFile/101/101>

https://www.ebay.com/itm/Duco-Cement-Multi-Purpose-Fast-Drying-Nitrocellulose-Household-Glue-Cement-1fl/253819114889?hash=item3b18cc5589:g:yFQAAOSw~Ltbdpno:rk:1:pf:0



Tarnation.

If the wax stays hot for long enough, I could put the whole casting in the vacuum chamber...

Tried the vacuum chamber technique. As you might expect, it didn’t work; the paraffin boiled vigorously and large voids opened up.

Perhaps I need to turn the whole situation upside down, with the part at the top of the mold.

I also had considerable difficulty in removing the printed part.

Gel-cast process 2

1. Melt paraffin wax at 85c.
2. Print parts and stick into mold box
3. Spray in mold release
4. Pour in wax
5. Immediately put in vacuum chamber
6. Pull a -27mmHg vacuum
7. Wait 20 minutes under vacuum
8. Release vacuum and wait another 20 minutes
9. Stir in 0.5% citric acid as a dispersant
10. Mix in alumina to create a 50%?/vol solution
11. Mix in 5% white glue
12. Pour into mold.
13. Dry glue at 45c for 30 minutes.
14. Melt away paraffin at 70c
15. Remove from mold.
16. Sinter to 600c at 1c/min.
17. Sinter as hot as your kiln can manage (over 1300c is best) at 2c/min.

Gel-cast process 3

1. Melt paraffin wax at 85c.
2. Print parts and stick into mold box
3. Spray in mold release
4. Pour in wax
5. Immediately put in vacuum chamber
6. Pull a -27mmHg vacuum
7. Wait 20 minutes under vacuum
8. Release vacuum and wait another 20 minutes
9. Stir in 0.5% citric acid as a dispersant
10. Mix in alumina to create a 50%?/vol solution
11. Mix in 5% white glue
12. Pour into mold.
13. Dry glue at 45c for 30 minutes.
14. Melt away paraffin at 70c
15. Remove from mold.
16. Sinter to 600c at 1c/min.
17. Sinter as hot as your kiln can manage (over 1300c is best) at 2c/min.

Wax sucks. It’s waxy, it’s irritating, and it gets everywhere.

Gel-cast process 4

1. Print molds
2. Pour in 5% white glue alumina solution
3. Mix
4. Vacuum
5. Dry at 50c
6. Sinter.

This still leads to shrinkage.

This caused extreme porosity, presumably due to the stirring.

I’ve heard tell that Kiln elements are damaged by combustible atmospheres, which seems plausible - however, because we pre-melt the PLA, there’s only a bit of residue remaining on the green, so this shouldn’t be a problem.

Gel-cast process 5

1. Print a negative mold of your desired part out of PLA. Make a reservoir and sprue with at least 1 extra volume of material.
2. Add 1 volume of warm water to 1 volume of calcined alumina.
3. Mix gently by hand without introducing air.
4. Add 1.5% (by mass, of the entire solution) gelatine.
5. Mix again, avoiding foaming.
6. Dry at 50-60c for a few hours - the exact amount of time depends on the size of the part, and the allowable temperature depends on the geometry of the part to avoid cracking.
7. Transfer to an aluminum pan and bake at 100c for 20 minutes to drive off any remaining moisture.
8. Melt PLA mold at 300c on an aluminium foil pan. The green is quite delicate now, so be careful.
9. Refresh aluminum foil pan and melt again.
10. Sinter to 600c at 1c/min.
11. Sinter as hot as your kiln can manage (over 1300c is best) at 2c/min.

Tried firing at 450c to melt off PLA, cool, remove from first layer of aluminum, fire on aluminum again to 500c to burn off residue, then all the way to 1000c.

Ramp rate was very high; 20-30c/min, roughly.

Large PLA feedthroughs exploded violently near 500c. I think a slow ramp rate will be required.

Parts really can't be moved before firing - they just crumble.

Fired to 900c over the course of about an hour and a half. All the plastic was fired away; the parts looked amazing. However, they crumbled immediately. Clearly a higher firing temperature is required; probably the addition of a few percent clay is called for.

Going to try the same again, but with the addition of slip.

Tried 5% (2 grams) of slip.

Firing with 1 element at “low”.

160c - 1 hour 4 minutes

Part temp: 173c

192.2 - 1 hour 10 min.

At “low”, temperature stabilized at 215c.

“Medium” also ineffective. 1 element set to “High”. Oof, high is too much. Back to medium.

Called it at 360c. Opened the lid, one big part on stilts exploded, but everything else looks fine. One section caught fire immediately.

Now going to fire to 1000c.

Fired to 1050c. Parts had a little more structural integrity, but not much.

I think I know why - there’s only about 6% solids in the slip. I’m going to try a much higher percentage now.

Gel-cast process 6:

20 ml of slip + 20ml of alumina. Zero gelatine as a test.



