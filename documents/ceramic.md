# Ceramics

[TOC]

### Issues with this article

- I'm an idiot with no experience in ceramics.
- This project was done under considerable time pressure while going to university, and so was not nearly as rigorous as it should have been. Maybe someday I'll produce some content I'm proud of
- I also had a total budget of <$200.

### A note on safety

Like most inorganic dusts, aluminum oxide powder isn't good for your respiratory system. It's not nearly as damaging as silica, but a respirator or fume hood is recommended. There have also been some studies showing some (admittedly tenuous) connection between aluminum inhalation and Alzheimer's.

If using a lost-PLA process, beware decomposition products. Perform the bakeoff and sintering process in a well-ventilated area.

The green body will almost certainly explode. This will send hot ceramic shrapnel in all directions.

Contact with 230v electric kiln elements will almost definitely kill you.

# The recipe

Works only for parts smaller than ~$5 \text{cm}^3$. Expect 0.5% shrinkage in X/Y; accurate Z (along mold gravity vector) may require grinding. Vacuum-safe, but permeable. If you have a CNC capable of machining steel dies, pressing may be a more desirable route.

This is by no means an optimal process, just one that I settled on.

1. Print a PLA negative mold of the part you'd like to print. 

   I was not able to overcome Z-axis shrinkage, and so extended the mold vertically to allow settling - standard reservoir/sprue arrangments did not work for unknown reasons. Avoid ceramic walls of inconsistent thickness, as they will likely crack while drying. 

   A test coupon that I had good results with is available here[^2]. 

   Thicker PLA walls will reduce deformation during drying, but will increase the likelihood of cracking during burnoff.

   ![mold](../media/mold.png)

2. Mix 1 volume $Al_2O_3$ with 1 volume warm water.

   You may need to reduce the water volume if excessive Z-axis settling and shrinkage is observed while drying. 

3. Add approximately 0.5 wt. % gelatine.

   The solution must have a sufficiently low viscosity in order to flow into the mold without resistance while simultaneously retaining sufficient green strength for firing. This value may require tweaking.

4. *(optional)* Add up to 5 wt. % $MnO_2$

   *sources indicate a sinter point depression, though no effect was observed in these tests*

5. Add a refractory binder if unable to reach pure alumina sinter temperature (~2000c).

   2.5 wt. % porcelain slip (XX% kaolin clay, XX% silica) was sufficient.

6. Add reinforcement to mold to taste.

7. Stir gently until homogeneous and pour into PLA mold.

   *alternately, if a low thermal conductivity is desired, beat the hell out of the mix to form a foam.*

8. Dry in an oven for ~6 hours at well above the gelation temperature - roughly ~70 C.

   Urethane molds can generally tolerate roughly 80 C, whereas PLA will begin to deform at ~65c. The precise drying temperature depends on the geometry of the part; variable thickness will cause differential drying and cracking.

   The green must be thoroughly dry; any residual moisture will cause it to explode.

9. Place the part in a graphite crucible or support it on tungsten wires.

10. Heat slowly with an oxy-acetylene torch to ~500c over the course of 1-2 minutes.

    The green is usually too delicate to be moved without a support structure, so PLA burnoff must be done in-place.



Future additions: urethane casting, more precise temperature regulation, carbon fiber reinforcement.

[^1]: wt. % of alumina+water solution.
[^2]: `files/coupon_style_7.fcstd` https://github.com/0xDBFB7/ceramics
[^3]: [Internal](../references/)  [External]()

[^3]: Xie, Zhi-Peng, et al. "A new gel casting of ceramics by reaction of sodium alginate and calcium iodate at increased temperatures." *Journal of materials science letters* 20.13 (2001): 1255-1257. [Internal](../references/Xie2001_Article_ANewGelCastingOfCeramicsByReac.pdf)  [External](https://link.springer.com/content/pdf/10.1023/A:1010943427450.pdf)

t[^1]

[^1]: Sgobba, Stefano. *Materials for high vacuum technology, an overview*. No. CERN-TS-2006-004. Cern, 2006. [External](https://cds.cern.ch/record/983744/files/p117.pdf)



### Preamble on motivation

#### Glass

[reliable seal matching percentage] Kovar has a coefficient of expansion. Based off these data, some anecdotes I've heard on the difficulty of obtaining a reliable glass-to-metal seal, 





#### Machinable/castable ceramics

[^1]: Rescor, Macor 780 et al [External](http://www.cotronics.com/vo/cotr/pdf/onepg700.pdf)

Many of Cotronics' materials display quite severe outgassing values. Some anecdotes on Fusor Forums regarding permeability also seemed to concur that these materials are generally not suitable for high vacuum.



As an integral part of a future product, the marginal cost of these parts was a key concern. A rod of Rescor/Macor might cost \$50, so a feedthrough might well cost \$10 after machining. Though is unacceptably expensive in my case.

In contrast, aluminum oxide is readily available and inexpensive. A 1 kg bag cost just under $14 at a local pottery shop.



In the interest of [Akin's 34th Law](https://spacecraft.ssl.umd.edu/akins_laws.html) (distinct from the *other* rule 34, which is largely unrelated to spacecraft design or even scientific inquiry as a whole), I figured I'd see what I could make on a limited budget.



### Mold and green binder

The problem with paraffin is that it melts at almost exactly the same temperature as the gelatine. This means that the gel must be almost completely dry (shrinking considerably) in the process.



Some problems with paraffin molds:

When casting fine details, it’s common for bubbles to form at the bottom. One way to fix this is to leave the heat on for a while, ensuring that the paraffin has time to flow into every nook and cranny. This, however, melts the hot glue sticking the mold together.

I guess I could just add a long sprue and reservoir to the mold to compensate for shrinkage.

Caulk/urethane molds

Caulking can be made to solidify quickly by way of glycerin.

## The mold and green body

#### Pressing

Pressing alumina is a common technique. You can either make a slurry (wet pressing), or just compact dry powder. 

https://nptel.ac.in/courses/112107085/module3/lecture5/lecture5.pdf

I don't currently have a CNC capable of making hard dies to reasonable tolerances and finish quality - I could perhaps make some aluminum dies.

#### Porcelain

Perhaps the simplest process to create ceramic green bodies, [slipcasting](https://en.wikipedia.org/wiki/Slipcasting) entails pouring a fluid solution of porcelain into a hygroscopic plaster mold. 

There are a few limitations to this process. As you might imagine, part thickness 

In addition, the plaster mold must be dried for many hours before it is sufficiently absorptive to allow the slip to gelate. This process can be accelerated by maintaining a flow of hot, dry air over the mold. The mold can't be heated very much, however, else the surface begins to calcine. Another interesting option is microwave drying of plaster, which is conveniently self-limiting.



USP #1 datasheet here



Like most sintering processes, you want to start with a green body. Much like trying to bake a cake with nothing but flour, you can’t just put a bunch of alumina powder into a mold and fire it; there won’t be the intimate contact between the particles that’s required for cohesion, and it’ll just crumble as soon as you remove it.

There’re a few different ways of making this green body.

<style>p.seven {
  border-style: solid;
  border-width: 20px 10px 10px 10px;
    }</style><p class="seven"><b>I feel like I learned something:</b><br>When characterizing trial-and-error processes, it might be useful to think of R&D in terms of software unit testing; that is, you want to create a sort of <a href=https://stackoverflow.com/help/mcve>MCVE<a></a> of your controls. As an example, it may be helpful to use the smallest batch size and the simplest test coupon likely to exhibit the same behavior as your final product. In this particular case, I began iterating the alumina recipe using my desired full-size feedthough part. The simplified test coupon required much less drying time and consumed 0.05x as much alumina - allowing me to try dozens of variations within the same batch.<br><br>On the other hand, making your test coupons overly simplistic may lead you down incorrect444 paths of inquiry. Had I not used a coupon with a cavity, I would likely not have discovered the difficulties inherent in casting perfectly void-free paraffin molds. It's a subtle tradeoff! I guess you just have to use your best engineering judgement.<br><br>This is probably obvious to all who know what they're doing - a select few whose ranks I am most definitely not a member of.</p>




So what else can we do? Well, we can cast it in a mold. Aluminum oxide isn’t soluble in water to any meaningful degree, but it does disperse into a suspension if it’s a fine enough powder. I’ve seen some discussion on the use of citric acid as a dispersant to improve ; however, I didn't observe any effects.

So now that we’ve got this suspension, we’ve got a few more options.

Paraffin

Urethane/caulk

#### Freeze casting



The unfortunate crystallizes when frozen tends to lead to large voids and high porosity in the final product, which is undesirable in a vacuum environment. t’s easy to get virtual leaks and stuff that way.

#### Gel-casting

You can also mix in some kind of binder that will burn off when fired. Really any organic binder will do, as long as it’s

sufficiently low viscosity to flow into the mold when mixed with your ceramic powder, sufficiently strong when "cured" to be cleanly extracted from the mold,

usable at sufficiently low percentages so that you don't get porosity or huge shrinkage after vaporization, and something that burns off cleanly during firing. Oh, and I have to be able to get my hands on the stuff easily.

#### 

- Alginate + calcium iodate[^3] (I couldn’t get my hands on the iodate in short order)
- Fancy water-soluble epoxies (tried regular epoxies, failed miserably as expected)
- PVA

[^3]: Xie, Zhi-Peng, et al. "A new gel casting of ceramics by reaction of sodium alginate and calcium iodate at increased temperatures." *Journal of materials science letters* 20.13 (2001): 1255-1257. [Internal](../references/Xie2001_Article_ANewGelCastingOfCeramicsByReac.pdf)  [External](https://link.springer.com/content/pdf/10.1023/A:1010943427450.pdf)

Dhara, Santanu, and Parag Bhargava. "Egg white as an environmentally friendly low‐cost binder for gelcasting of ceramics." Journal of the American Ceramic Society 84.12 (2001): 3048-3050.

g[^3]

Some examples are alginate with calcium iodate , , PVA (either powder or school glue).



I also talked to an expert in the field of organic binders. Fluffy, delicious organic binders, specifically. She gave me this arcane tome,

das neue koch buch 

saying that I’d find all my answers within. And you know what? Mom was right. Look here, at page 187:



Now, my 1930s German is a little rusty, but I managed to find a modern translation.



No, I didn’t make that up - well, not the paper, that is. That’s published. Frankly, I’m as surprised as you are.






> oh the redhead said you shred the cello, and I'm -

#### Jello

[^4]: Stoner thermoplastic mold release, McMaster-Carr #1409K44 [External](https://www.mcmaster.com/1409k44)

I was not able to replicate their results. The fully gelated green body was far too delicate to be removed from the mold. However, my modified process is quite effective. It involves drying at 70c

<video src="../media/20181110_213428.mp4"></video>

When poured into a small test tube, the mix ratio was very obviously excessively wet.

The amount of gelatin used was too low to reliably measure on my $14 milligram balance.



at this juncture I would like to point out the existence of the Gelatine Handbook[^4]. 350 pages of excruciating detail on every possible intricacy of the gelatine production process. 

[^4]: Gelatine Handbook [Internal](../references/Gelatine_Handbook_tagt.pdf)  [External](https://www.docollection.me/doc/Gelatine_Handbook_tagt.pdf)

Of Englishe dogges: the diuersities, the names, the natures, and the properties https://books.google.fi/books?id=y8kCAAAAYAAJ&pg=PP7&hl=en&authuser=0#v=onepage&q&f=false





Something quite interesting can be observed with this open-cavity mold. No meniscus is present.

Drying at 70c, however, produced a very strong green body:

<video src="../media/processed/20181110_143321.mp4"></video>

My results differed from theirs quite significantly. With too many 



#### Drying

Different cross-sections tend to dry at different rates, causing a differential expansion and contraction. At 70c, the thin mounting lobes on the part above invariably cracked before the entire body was dry. 



#### Bubbles & Porosity

The USP pottery plaster that I used for my porcelain tests

I inexplicably mentally transferred that requirement to my alumina tests, which led me to, er, *whip* the alumina slurry. 

<video src="../media/processed/20181121_134556.mp4.mp4"></video>

This process might actually be useful for producing a sort of low-density insulating alumina foam; the rheology of the gel produces a very porous structure. It also represents the antithesis of my desired end goal.



The gelatine in the gel-casting process

Porosity is




<video src="../media/20181121_135626.mp4"></video>

There's a slight problem that arises when degassing pseudoplastics like gelatine. As moisture evaporates, the solution is chilled, which greatly increases the viscosity, making the solution ever harder to degas.

https://abbess.com/wp-content/uploads/2016/03/Degassing-Mixing-V2-Secure.pdf

In any case, stirring the colloid gently a few times is more than sufficient to produce a homogeneous suspension of alumina.





## The refractory binder

#### Manganese dioxide

[^1]: Luks, Daniel W. "Vitreous high alumina porcelain." U.S. Patent No. 2,290,107. 14 Jul. 1942. [Internal](../references/US2290107A.pdf)

[^2]: NileRed on Carbon-Zinc batteries [External](https://www.youtube.com/watch?v=XC5q9mDKUCo)

You may know me to be quite critical of the patent system. Despite having a patent pending, I am quite confident that  

But this patent is prime example of how the system could work. This dude ran nearly 4500 tests.



Luckily, $$MnO_2$$ is readily available in the form of carbon-zinc batteries.[^2] I ripped a few apart

#### Clay



## Kiln in the name

Now we come to the matter of heating these. Prometheus notwithstanding, 

#### Electric kilns

This kiln draws 5.5 kilowatts while operating, and can reach roughly 1300c over about 3 hours.

Most of the elements were broken.



<video src="../media/20181111_162140.mp4"></video>

A high-temperature lab would be incomplete without a Molybdenum disilicide kiln.`zirconia sintering kiln`seems to be a useful keyword.



#### Vacuum furnace

There's

If convection can be eliminated, our problem becomes very simple. By Stefan-Boltzmann (I asked him personally!), a generous area of 5 cm^2, we need about
$$
\text{P}=\text{R} \text{E} \text{A} \text{T}^4 = 5.67\times10^{−8} \times (1800)^4 \times 0.5 \times 2*\pi*0.01\text{m}^2=942\text{ watts}
$$
That's really quite insignificant.

However, at 5% the thermal conductivity of copper, transferring heat from a tungsten heater to the bulk of the ceramic is quite a difficult task.

In addition, my high vacuum chamber was not serviceable during this period. which can only attain a vacuum of around 50 Pa - not sufficient for this process. This was assembled 2 hours before leaving for finals

<video src="../media/20181211_173959.mp4"></video>

 I had to use the vacuum tube as a high-current feedthrough. 



#### Gas firing

After . Lo and behold, the fragment took on the desired glassy texture and increased in strength considerably. 



I supported the part with some 3/32" Tungsten TIG rods. 

#### Electric arc furnace



### Measuring temperature

McMaster carr thermocouple

The values from this thermocouple

#### Ratio pyrometry

I was planning on building a ratio pyrometer 

A problem arises when the emissivity of the substance varies throughout the frequency range - a "Selective Radiator". http://gsp.humboldt.edu/olm_2015/courses/gsp_216_online/lesson8-1/emissivity.html , but these 

Spectrometry





# The finished product

Here are the best parts I was able to produce.

![20181212_182620_HDR](../media/20181212_182620_HDR.jpg)



t's not going to win a beauty pageant, and it's almost definitely not sufficiently impermeable to be useful as a vacuum feedthrough. However, X and Y dimensional accuracy was superb, with only ~1% shrinkage. 0.3mm of the desired dimensions. Z dimensional accuracy was quite poor - the addition of slip increased the viscosity and caused a meniscus to form on the inside wall of the mold. 

As a light-duty refractory support, however, it's acceptable.



The shiny patch in the middle is molten glassy alumina, where I brought the torch far too close to the part. More rigorous process controls would be required in order to produce a truly usable part. Some sort of heat spreader would be excellent; I've since purchased a graphite crucible, which might improve the sinter quality. 

The two green lines are $WO_3$, residue from the 1/16" tungsten rods I used to support the part while firing.

![Screenshot from 2019-02-10 15-27-12](../media/Screenshot from 2019-02-10 15-27-12.png)

![Screenshot from 2019-02-10 15-27-45](../media/Screenshot from 2019-02-10 15-27-45.png)

![Screenshot from 2019-02-10 15-29-01](../media/Screenshot from 2019-02-10 15-29-01.png)

​	Kinda sucks.

In any case, I abandoned this project at this point. Alumina parts are a key component in a certain product that I am developing; I merely needed to convince myself that I would be able to vertically integrate this process within a certain timeframe.

I carefully sectioned (rather, broke haphazardly) a few of the most successful parts. Here are a few micrographs of Batch 12 and 13.

![20181212_195540.mp440](../media/processed/20181212_195540.mp440.jpg)

Note the striations captured from the original PLA mold. Extremely fine feature definition and low porosity. 10/10.

![20181212_195540.mp4](../media/processed/20181212_195540.mp4.jpg)

Here's the outside face.

I performed some digital strength tests:

<video src="../media/20181212_200256.mp4"></video>

The alumina had the strength of a particularly stale tea biscuit - a far cry from the results reported in the original gelatine paper. I hypothesize that this is due to my abysmal sintering setup, and not any fundamental mixture limitation.

Interestingly, the low-slip batch was noticeably stronger.



### Addendum: Brazing



#### Anodic bonding / electroadhesion

Followers of my youtube channel will have learned of my brief affair with electroadhesion. While easily achievable with glass/copper interfaces, I was curious as to whether this process would be practical to perform with alumina. And indeed it is! I have found precisely one mention of successful anodic bonding to the beta allotrope/phase of alumina, leading me to believe that this process is beyond my capabilities and patience. [paper here]. 

https://ceramics.onlinelibrary.wiley.com/doi/abs/10.1111/j.1151-2916.1979.tb12726.x

one more paper though

### Addendum: 

Cutting 





Budget: $200.

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

oh the redhead said you shred the cello, and I'm -

Garrido, L. B., and E. F. Aglietti. "mullite-zirconia COMPOSITES: Effect of dispersants on slip and cast properties."

Porcelain slip generally relies on the plaster absorbing moisture from the material. In my case, the green would be far too thick to absorb the water anyhow. Porcelain shrunk significantly when drying at 85c. The green was almost perfect, except for the shrinkage. I bet a closed mold with a sprue and reservoir would fix that. However, Alumina has some properties that I need for other sections of the system, so I figured I'd drop porcelain for now and focus on that.

Glass is also sometimes acceptable. However, some parts of my chamber will have to withstand somewhere around 1600c, so having the ability to make ceramic parts would really be invaluable.

You can press and sinter alumina pretty easily. There's a number of sub-techniques here, with wet or dry die pressing, hot or cold isostatic, etc. The main limitation here is that you need to make press dies out of quite a hard material. You might be able to get away with aluminum for a few shots, but usually these dies are made of some sort of hardened steel. My dirt-cheap 6040 CNC is not going to cut it, what with its 50 thou chatter and whatnot.



Simple freeze-casting is possible, where an aqueous solution of alumina is frozen; however, crystal formation leads to high porosity and defects.

<https://link.springer.com/content/pdf/10.1023/A:1020718225164.pdf>

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

https://www.scsolutions.com/wp-content/uploads/paper.gelcast2.pdf:

“The current empirically-guided drying process for parts which are about an inch thick can take several days, and is the longest stage in the gelcast manufacturing process.”

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



# Wanna chat about this? Hit me up on twitter @0xDBFB7, or on irc.0xDBFB7.com:6667 #general.