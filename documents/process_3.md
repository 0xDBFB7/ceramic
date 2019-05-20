#### Deprecated, see process 5.

Limitations:

- See [the finished product](#the finished product) to confirm that the part quality is sufficient for your needs.
- This can only function for parts smaller than ~$5 \text{cm}^3$ due to differential heating. An [alternate heat source]() would alleviate this requirement.
- Expect 0.5% shrinkage in X/Y; accurate Z (along mold gravity vector) may require grinding. 
- Vacuum-safe (volatiles are removed, as almost all carbon-carbon bonds are broken), but highly permeable. 
- If you have a CNC capable of machining steel dies, pressing may be a more desirable route.
- This is by no means an optimal process, just one that was attainable in my lab.

<hr>

1. **Print a PLA negative mold of the part you'd like to produce.** 

   I was not able to overcome Z-axis shrinkage, and so extended the mold vertically to allow for settling - standard reservoir/sprue arrangements did not work for as yet unknown reasons. Avoid ceramic walls of inconsistent thickness, as they will likely crack while drying. 

   A test coupon that I had good results with is available here[^coupon]. 

   Thicker PLA walls will reduce deformation during drying, but will increase the likelihood of cracking during burnoff.

   ![mold](/home/arthurdent/deep/ceramics/media/mold.png)

2. **Mix 1 volume pure $\text{Al}_2\text{O}_3$ with 1 volume water at 45 deg C.**

   You may need to reduce the water volume if excessive Z-axis settling and shrinkage is observed while drying. 

3. **Add approximately 0.5 wt. %[^1] gelatine.**

   The solution must have a sufficiently low viscosity in order to flow into the mold without resistance while simultaneously retaining sufficient green strength for firing. This value may require tweaking.

4. *(optional)* **Add up to 5 wt.** **%** $\text{MnO}_2$ 

   *See [refractory binder](#The refractory binder).* *Sources indicate a sinter point depression, though no effect was observed in these tests*. 

5. **Add a refractory binder if unable to attain pure alumina sinter temperature (~2000c).**

   2.5 wt. % porcelain slip was found to be optimal[^slip]. Pure clay would be preferable; the dispersants in slip caused an undesirable meniscus effect. 

6. Add composite reinforcement to taste. 

   *see future additions.*

7. Stir gently until homogeneous and pour into PLA mold.

   *alternately, if a low thermal conductivity is desired, beat the hell out of the mix to form a foam.*

8. Dry in an oven for ~3 hours per cubic centimeter at well above the gelation temperature - approximately 70 deg C.

   Urethane molds can generally tolerate 80 C, whereas PLA will begin to deform at ~65c. The precise drying temperature depends greatly on the geometry of the part; again, variable thickness will cause differential drying and cracking at high drying rates - see[^drying].

   In any case, the green must be thoroughly dry. Any residual moisture will cause it to explode.

9. Place the part in a graphite crucible[^8] or support it on tungsten wires.

10. Heat slowly with an oxy-acetylene torch to 500 C over the course of 1-2 minutes.

    The green is now too delicate to be moved without the support structure, so PLA burnoff must be done in-place.

11. Heat to approximately 1800 C. Hold temperature for 2-3 minutes. The entire part must glow white-hot.

    Determining the exact temperature is quite difficult and seems to be unnecessary. See [measuring temperature](#measuring temperature).

<hr>

Future additions: 

- [ ] Urethane casting
- [ ] Graphite heat spreader
- [ ] Quantitative sinter temperature measurement
- [ ] Lock down ideal gelatine percentage
- [ ] Carbon fiber cloth reinforcement testing

<hr>

[^1]: wt. % of alumina+water solution.
[^coupon]: `files/coupon_style_7.fcstd` https://github.com/0xDBFB7/ceramics
[^3]: [Internal](../references/)  [External]()
[^alginate]: Xie, Zhi-Peng, et al. "A new gel casting of ceramics by reaction of sodium alginate and calcium iodate at increased temperatures." *Journal of materials science letters* 20.13 (2001): 1255-1257. [Internal](../references/Xie2001_Article_ANewGelCastingOfCeramicsByReac.pdf)  [External](https://link.springer.com/content/pdf/10.1023/A:1010943427450.pdf)
[^1]: Sgobba, Stefano. *Materials for high vacuum technology, an overview*. No. CERN-TS-2006-004. Cern, 2006. [External](https://cds.cern.ch/record/983744/files/p117.pdf)
[^drying]: "The current empirically-guided drying process for parts which are about an inch thick can take several days, and is the longest stage in the gelcast manufacturing process." Ghosal, Sarbajit, et al. "A physical model for the drying of gelcast ceramics." *Journal of the American Ceramic Society* 82.3 (1999): 513-520. [internal](../references/drying.pdf) [External](https://www.scsolutions.com/wp-content/uploads/paper.gelcast2.pdf)
[^slip]: Sial 124M slip MSDS (~3.5% silica, ~20% kaolin clay) [Internal](../references/MSDS124M.pdf) [External](https://tuckerspotteryeshop.com/wp-content/uploads/msds/clay/MSDS%20124M.pdf)
[^8]: Readily available on eBay for $20.
[^9]: Green TIG rods are an excellent source

