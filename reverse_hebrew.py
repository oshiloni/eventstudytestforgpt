# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 09:59:26 2023

@author: omer
"""
import re

text = "  


   תילכלכ תעד תווח


  


   םרגנש ילכלכה קזנה תדימא

    טידרק טנוי   ת ו ינמ ילעבל

  

  

  


  


  


  


  


  

  

  

  

  

  2022 ינוי


  


  


  


  


   - 2 -  

 

  

  ה ח מומ  תעד תווח

  

  

   ונמ דעליג   :החמומה םש

  מ"עב םיסנניפ ורקאמ    :ותדובע םוקמ
  .פ.ח515618403
   המוק ,קרב ינב ,9 אבכוכ רב16

  

  וז תעד תווח שיגהל ,ריאמ ןב רחשו םריבא קחצי ןידה יכרוע ידי לע יתשקבתנ ,ונמ דעליג ,הטמ םותחה ינא

  וא  ""  :ןלהל)טנוי    םייסנניפ  םיתוריש  טידרק  טנוי  דגנכ  תיגוציי  הנעבות  רושיאל  השקב  תרגסמבמ"עב

  םוסרפ יא" לע הרבחה תעדוה  תובקעב    תוינמ ילעבל םרגנש קזנ ןיינעבבהרבח,   יאשונו ,"הרבחה(",הרשמה

    דע לש ךרעומ ףקיהב תויפסכ תומאתה יא תובקעב תאזו "7.6  תנשל ןושארה ןועברל םייפסכ תוחוד2022

 וניאש םוכסב םיפסכ הרבחה תאמ ,הרואכל  ל טנ ,רזא יחצ רמ ,הרבחה ל"כנמ יכ ,ששח תובקעבו ₪  ן ו י לימ"

   . הרבעוהש רושיאל השקבב טרופמכ לכהינויעל  וא"םיעוריאה"(,  :ןלהל) ""עוריאהל יתוהמהרבח"

  החרטה רכש .ןיפיקעב וא ןירשימב ,םמעטמ ימב וא הדובעה ינימזמב וא הרבחב תולת וא רשק לכ יל ןיא

  וא ןירשימב  הנתומ וניאו שארמ עובק וניה הדובעה ינימזמ ןיבל יניב םכוסש יפכ ,וז תעד תווח תנכה ןיגב

  יטפשמה ךילהה תחלצהב ןיפיקעב.

  ילילפה קוחה תוארוה ןיינעלש בטיה יל עודי יכ ריהצמו טפשמ תיבב תודע םוקמב וז יתעד תווח ןתונ ינא

  יתתנש הרהזאב תודע ןידכ ידי ילע המותח איהשכ וז יתעד תווח ןיד ,טפשמה תיבב הרהזאב רקש תודע רבדב

   .טפשמה תיבב

  

     תעד תווח ןלהל.י

  

  

  

  

   
    _____________                                                    .2022.612        
   המיתח                                                                     ךיראת          

     









   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 3 -  

 

    םיניינעה ןכות

  

  יללכ  .1

 עקר  .2

  תעדה תווח תיצמת  .3

  תעדה תווחב היגולודותמ  .4

  Event study - market model קושה לדומ תועצמאב עוריא רקח  .5

  לדומל סחיב  רחאל הינמה יעוציב חותינחווידה  .6

  תגצוימה הצובקה ירבחל קזנה תכרעה  .7

  תשקבמל קזנה תכרעה  .8

  עדימ תורוקמ  .9

  בתוכה לש ןויסנו הלכשה תיצמתי 10.

   

   

 

  


























   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 4 -  

 

 

  יללכ  .1

  טידרק   טנוי   תוינמ ל םרגנשיקיזחמ     ק זנהילכלכ,ה   לש   ו ת ו מיכו   ו מ   ת ל אשויק תניחבב תקסוע תעדה תווח

  :אתכמסא)    ם ו י מ הרבחה ת1.6.2022ב וחוודו הרבחב ויהש םיעוריאעדוהו  לשב  מ"עב םייסנניפ םיתוריש

  יא  .  יפינסמ דחאב תויפסכ  תומאתה  יאל  ששח  הלועש  ךכ  לע  ,ךכל  ךומסבוהרבחה  (2022-01-068572

  תעדוהב   ףסונב  .₪ ןוילימרסמנ    דע7.6  5  כ-   לש ךרעומ ףקיה לע  הליחתב    תויפסכה תומאתההנודמע

  תפוקב   קדובה ךרעש הקידבמש ךכ לע (,  :אתכמסא)2022-01-069349ינוציחה    םוימ הרבחה2.6.2022

  םיאצממ ולגתה הקידבב ןכ ומכ .₪ ןוילימ    לש ךסב תרצנ ףינסב ונתינש תואחמה תורסח הרבחה7.7

  םוכסב םיפסכ הרבחה תאמ הרואכל לטנ ,רזא יחצ רמ ,הרבחה ל"כנמ  יכ ,ששח םייק םהיפל םיינושאר

  תוחוד  םוסרפ  יכ העדוה הנתינ רומאה לע ףסונ  .ודיקפתמ העשוה רזא רמ יכו .הרבחל יתוהמ ונניאש

   .הנכשמית תוקידב העדוה הנתינ ןכה .םימי רפסמ רבכש  םוסרפה ןכאו בכועי הרבחהבכועמ

   ,ם ל"כנמ דגנ םישקה תודהחה לעו תומאתהה יא לעשהרבחה  םיעיקשמה רוביצל  ליג רשאו   ויחוםי,דה

   .תועדוהה רחאלש רחסמה ימיב  טנוי תיינמ  יוושב  תודירילתודח  ליבוהו  ,םינד ונא  בםה עוריאהםי

   :םייטנוולרה סוחיה ידדמל סחיב  טנוי תיינמב םיימויה םייונישה ןלהל

  את דדמ-125   םיסנניפ  דדמ  םיסנניפו חוטיב את דדמ  טנוי 
          1.04% 2.29% 1.62% -22.28% 01/06/2022 

          -1.09% -1.29% -1.38% 2.87% 02/06/2022 

          0.70% 1.11% -0.05% -1.96% 06/06/2022 

          -1.19% -0.78% -1.38% -3.89% 07/06/2022 

   

  הדירי אלל תאזו    לעמ24.6%ב    תרבח תיינמ החנצ העדוהה רחאטנויש רחסמה ימיל    ,רבטצמבבתעברא

    . םייטנוולרה סוחייה ידדמ דחא ףאהרבחלב תיתועמשממ

  את דדמ-125  םיסנניפ  דדמ  םיסנניפו חוטיב את דדמ טנוי 
            1.04% 2.29% 1.62% -22.28% 01/06/2022 

            -0.07% 0.97% 0.21% -20.04% 02/06/2022 

            0.63% 2.09% 0.17% -21.61% 06/06/2022 

            -0.57% 1.30% -1.22% -24.67% 07/06/2022 

   

   עוריאםי.ה  תובקעב 25.4%  הדרי   תיינמטנוי  תעפשה לורטנב ,,ונאצממ יפ לעקושה

   -כ םיקיזחמו   ילעב םניאש  תוינמה ילעב ללכ הניההטילש  ,רושיאה תשקב יפ לע תגצוימה  הצובקה

   .₪  ןוילימ  5.1  כ  לע דמוע  ונאצממ  יפ  לע  וז  הצובקל  םרגנש  ללוכה  קזנה-   .הרבחה תוינממ  34.37%

  

  עקר  .2

  .  ה ר בחכתיטרפ  31.5.1990  ב לארשיב הדסונו הדגאתה מ"עב םייסנניפ םיתוריש טידרק טנוי תרבח- 2.1.

  קחציו ,וסנפ יש ,קיזייא המלש םניה הטילשה ילעב  .תירוביצ הרבחל הרבחה הכפה    תנשב1994

    .הרבחה  תוינממ    -65.63%כ   וידחי     רשא   (םיקיזחמהרבחה      שמשמהל"כנמ   רזא  (יחצ))

   

 

   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 5 -  

 

 :םיירקיע תוליעפ ימוחת ינשב תקסוע הרבחה 2.2.

  תואוולה  ןתמב  תקסוע הרבחה יארשא ןתמל ןוישיר תרגסמב  –   יאקנב ץוחה יארשאה םוחת 

  .ךורא חווטל תואוולהו תואחמה ןויכינב , םיקסעל תואוולה ,תוינכרצ

  תוחוקלל  הקינעמ  הרבחה  יסנניפ  סכנב  תוריש  ןתמל  ןוישיר  תרגסמב    ח"טמ  תרמה  םוחת– 

   .ח"טמ תורמה לש םיתוריש םינוש

   : ל ןוכנ טנוי תרבחב תוקזחאה הנבמ2.6.2022













  

   היקסעל הלש  תובישח תא השיגדמ הרבחה ,  תנשל2021ןיטינומה הרבחה לש םייפסכה היתוחודב 2.3.

  :םיפיעס רפסמב

  תריצי"  :ןיטינומה  ףיעס  תחתב  הסינכ  ימסחו  םייטירק  החלצה  ימרוגב  קסועה    ףיעסב7.6 

  "הייפואו תוליעפה גוס רואל הרבחה לש תוליעפה םוחתב יטירק החלצה םרוג הווהמ ןיטינומ

  תוליעפ  ,רומאכ"  :  ףיעס  תתב18.2.2    הרבחהתנייצמ   םייפנע  םינוכיסב  קסועה    ףיעסב18.2 

  ןיטינומב העיגפ .םיליבקמה םהיקסעב םג הילהנמ לש םינשה בר ןיטינומה לע תתתשומ הרבחה

  העיגפל איבהל הלולע םיירוטלוגרה םיפוגה וא תוחוקלה לצא ןימאו ביצי יסנניפ דסומכ הרבחה

 "הרבחה תויחוורבו תואצותב

   :2018  -ב ףיקשתה תכירכ לע הרבחה הריהצה ךכ ,ףסונב 2.4.

  םוחתב הרבחב העקשה םינייפאמה םינוכיסב הכורכ הרבחה לש ךרעה תוריינב העקשהה"

  הערה  ,יטילופ  ,ינידמ  ,ינוחטיבה  בצמב  הערה  :םיילכלכ  ורקמ  ןוכיס  ימרוג  :הקוסיע-

 :םייפנע  ןוכיס  ימרוג   ;ח"טמל  הפישחו  ןומימ  תורוקמב  תולת  ,קשמה  בצמב  תיתוהמ

  ןדבוא ,הרבחה תוליעפ םוחתל םייטנוולר םיללכו תוינידמ ץומיאו יושיר ,הקיקח ייוניש

  תולת ,הרבחל ןומימ סויג תלוכיב תולת :הרבחל םידוחיי ןוכיס ימרוג ;תורחתו ןיטינומ

   ." היבגו חתפמ ישנאב

  

  הרבחהמ םרוג י"ע  "ינושאר ןוכדע" לבקתה ,ברעה תועשב    םויב הרבחה יחוויד יפ לע29.5.2022 2.5.

  יאל ששח הלוע ,ודי לע ועצובש תוימינפ תורקבל םאתהבש  הרבחה לש ןוירוטקריד תבישי ךלהמב

  .הרבחה יפינסמ דחאב תויפסכ תומאתה


   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 6 -  

 

  תוכלשהה ללכו אשונה תניחבל ,יולת יתלב ינוציח קדוב תונמל ןוירוטקרידה טילחה ךכל םאתהב 2.6.

 .רומאכ תומאתהה יאמ תועבונה

  ינוציחה   ודקבה י"ע םייטנוולרה םימרוגה לואשת לש ינושאר בבס תמלשה רחאל    םויב31.5.2022 2.7.

  סיסב  לע  .תויפסכ  תומאתה  יאל  תוששחה  תא  ססבל  ידכ  םהב  שיש  םיינושאר  םיאצממ  וגצוה

  ולא תויפסכ תומאתה יכ ,ינושארו ימדקמ ןפואב ינוציחה קדובה ךירעה םיינושארה םיאצממה

  .₪ ןוילימ  דע7.6 5 כ לש ךרעומ ףקיה לע תודמוע-


  םייפסכה תוחודה םוסרפ רושיא תא  ב כ על  הרבחה ןוירוטקריד טילחה םיינושארה םיאצממה רואל 2.8.

 .תורומאה תומאתהה יאל ףיקמ הקידב ךילהת  תמלשהל דע   תנשל ןושארה ןועברל2022

  ילבמ תאזו םיעוריאה לע    חווידב החוויד הרבחהידיימ    העשב00:11,  תוצח רחאל ,  םויב1.6.2022 2.9.

  .ךכל רבעמ ףסונ עדימ לכ אללו םישעמב םידושחה םימרוגה תא ןייצל

   לש22.27%. תודח תודיריב הז יקלח עדימ סיסב לע להנתה  הרבחה תוינמב רחסמה םוי . 2.10

  תובקע  , י ת והמ עוריא רבדב חוויד םסרפל התנווכב יכ העידוה הרבחהב    ה ע שב10:17    ם ו י ב2.6.2022 . 2.11

  .הרבחה תוינמב רחסמה חתפנ אל תאז

  קדובה  לש  םיינושאר  םיאצממל  ךשמהב  ןוכדע"  הרבחה  המסרפ  םויה  ותואב    העשב13:05 . 2.12

  תורסח הרבחה תפוקב יכ ןכדע ינוציחה קדובה יכ תחוודמ הרבחה הז חוויד תרגסמב ."ינוציחה

 .₪ ןוילימ  לש ךסב תרצנ ףינסב ונתינש תואחמה7.7

  כ לע דמוע ימצעה הנוה , המסרפש םינורחאה םייפסכה תוחודל ןוכנ יכ ןייצנ הז רשקהבהרבחה  . 2.13

 .הרבחה לש ימצעה הנוהמ  כ10% ה ווהמ מאהרו  ש ךכםוכסה  ןוילימ₪. 77.7

  רתאל חילצת אל הרבחה םא יכ ,ובייחתה ,קיזייא המלשו וסנפ יש הטילשה ילעב ,ךכ תובקעב  . 2.14

  ךס תא הרבחל הטילשה ילעב וריבעי ,ןקלח וא ןלוכ ,  ף ו ס2022ל דע תורסחה תואחמהה תא תובגלו

   .תובגל החילצה אל הרבחהש תורסחה תואחמהה

  יחצ רמ הרבחה ל"כנמ יכ ,ששח םייק םהיפל םיינושאר םיאצממ ולגתה יכ הרבחה הנכדע ,ןכ ומכ  . 2.15

  שרדנ ןכ  לעו .הרבחל יתוהמ ונניאש םוכסב םיפסכ  הרואכל ,לטנ ,הב הטילשה ילעבמ וניהש ,רזא,

  םימוכס םתוא םהמ תושרופמ הנייצ אל הרבחה  .הרבחה תאמ ,לטנש לככ ,לטנש םוכס לכ בישהל

  .הז רשקהב "הרבחל םייתוהמ םניאש"

  ההשי ,רוריבה רמגל דע יכ ,שקבתה רזא יחצ רמ.השפוחב . 2.16

  םירומאה םיעוריאה לש תויאנובשחה תוכלשהה תא תנחוב איה יכ התעדוהב הרבחה הפיסוה דוע . 2.17

 . ת ו מדוק  תופוקתל  םייפסכה תוחודה לע םתעפשה תאו ליעל

  ךא ,הלש  םייתפוקתה  תוחודה  תא המסרפ אל םג ךא תופסונ תורהבה הרבחה הקפיס אל זאמ . 2.18

  .תופסונ תוקידב תולהנתמ יכ הריהבה

  תעדה תווח תיצמת  .3

  אלש עדימה תניחבמ ןה ,םירומאה םיעוריאה תובקעב הרבחב םיעיקשמל  םרגנש קזנה תדימאב ונניינע

  לע רומאה עדימה לש העפשהה תניחב י"ע תאזו ןיטינומב העיגפה תניחבמ ןהו הרבחה יבגל עודי היה

   .הינמה רעש

   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 7 -  

 

  םיינגוסקא םיעוריא לרטנמה   Study,  לדומב שומיש ידי י"ע העצוב וזEvent  תעד תווחב  קזנה תדימא

  ילכלכ יופיש וניה    םוימ  חווידה תרגסמב  הטילשה ילעב ונתנ ותוא יופישה יכ  ןייצנ2.6.2022  הרבחל.

  הרבחה  לש    ןדבואמ  םרגנה  קזנ וניה  תוינמה  ילעבל  םיעוריאהמ  םרגנה  קזנה  יכו  ,דבלבןיטינומה

  התדימע יא תובקעבו ל"כנמה דגנכ ולעוהש תודשחה תובקעב ,הלש תימינפה הרקבב םייוקילה תובקעב

  דחאה  :םיינשב  וניה ןאכ  ןחבנה  קזנה  , לעןכ   .  םייפסכ  תוחוד םוסרפל  תוירוטלוגרה  תושירדבדעומב

  םייק הזה עדימה היה ול הינמה ךרעב ינשהו ,הינמה ךרע תדיריב םלוגו םיעיקשמה לומל עגפנש ןיטינומב

   .ןכל םדוק םיעיקשמה ידיב

  עבונהו  עוריאונממ רשקב  הרבחה תוינמ ילעבל םרגנשל    קזנההרישיו הינמב העיגפה  ונאצממ יפ לע,

    .   םרטעוריאה  הרבחה  תיינמ  רעשמ  25.4%  של  רועישב  ונדי  לע    ,ךרעומקושה  תעפשה  לורטנבו

  

 תעדה תווחב היגולודותמ  .4

  הרבחה  תוינמב  יעיקשמל  םרגנש  קזנה  תאו  עוריאה  תעפשה  תא  םינחוב  ונא  וז  תעד  תווחבם 4.1.

  םוימו    םוימ1.6.2022  ידיימהםי    ביבסחווידהםי  היינמה תדירי תדימא תועצמאב תאז  ויתובקעב,

 הרבחה ל"כנמ דגנכ תודשחהו תומאתהה יא תודוא. 2.6.2022

  תעפשה) הרבחל םיינגוסקא םייוניש תעפשה לורטנל היגולודותמב םישמתשמ ונא רומאה ךרוצל 4.2.

  רקחל תיעוצקמה תורפסב לבוקמ רשא   ילניקמ לש1   Study  לדומב שמתשהל ונרחב .(קושהEvent

  .םיעוריא תעפשה

  :םיקלח השולשל קלחתמ לדומה

 ע ו ר יאה  םורט  ה פ ו קת יהוז   ("הדימאה תפוקת" :ןלהל) (2 window) הדימאה תפוקתestimation  .I

  .הרבחה לש ךרעה תוריינ לע קושה לש "הליגר"ה העפשהה לש הכרעה םיעצבמ הבש

  תמועל  לדומה  יפ  לע  היופצה  האושתה  ןיב  רעפה  תא  םיקדוב  עוריאה  ןולחב  :עוריאה  ןולח II.

  לע םייופצה םייונישהמ קהבומ ןפואב םינוש עוריאה תובקעב םייונישה םאהו .לעופב םייונישה

  .לדומה ידי

     עוריאה  רחאל  עוריאה  לש  תרבטצמה  העפשהה  תניחב  :"עו ריא  טסופ"  ןולח.ומצע  .III

   

       

 

       

       

  תמצוע תא אוצמל תנמ לע   

  ןיבל  לדומה  ןיב  רעפה  תא    ןמז  לוורטניא  לכב  םינחוב  ונא  הרבחה  לע  עוריאה  לש  העפשהה(םוי)

   :הינמה לש לעופב םיעוציבה

 
 
 

 

  1
 Event studies in economics and finance – A.craig MacKinly Jornal of economic literature 
  
   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ s ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 8 -  

 

  קהבומ ןפואב םינוש םה םאה םיקדובו  םימיה ךרואל ל"נה םירעפה תא םימכוס ונא ןכמ רחאל

  :לדומהמ רבטצמה רעפה בושיח  .לדומהמ





  תמר תא םיקדוב ונא  , ןקתה תייטסבוהמיאתמה  רפסמב בשחתמהםילוורטניאה   ןחבמ תועצמאבt

  ,ונלביקש האצותה המכ דע תקדובה תיטסיטטס הקידב וניה    ןחבמ .לדומהמ הייטסה תוקהבומt

  ןחבמ .תירקמ הניא האצותהש רמולכ ,ספאמ קהבומו יתוהמ ןפואב הנוש ,דמאנה לדומהמ הייטסה

    .  רפסמבו  ,ןקתה  תייטסב  ,(תרבטצמה  הייטסה  לדוג)  האצותה  הבוגב  בשחתמ  הזםילוורטניאה

  האצות הניא ונלביקש האצותהש ךכל תורבתסהה השעמל איה ןחבמהמ תלבקתמה תוקהבומה תמר

   .תירקמ

  

  תא םידמוא ונא הז לדומב  ;( קושה לדומ וניה ונשמתשה וב הדימאה לדומ :OLSהדימאה לדומ)

  ינפל תעצבתמ וז הדימא .רחבנש סוחייה דדמ לש יונישה ירועישל סחיב היינמה לש יונישה ירועיש

   .הרבחה הנבמב םייונישמ ענמיהל תנמ לע היד הכומס ךא ,עוריאה תורק




  

  םויס דע ךשמנ ותעפשה תדימא ךרוצל עוריאה ןולחו    ך י ר אתב לחה עוריאה1.6.2022  : ע ו ריאה תרדגה

 יכו חרכהב ומייתסה אל עוריאה לש תואלמה ויתוכלשה יכ ןייצנ הז רשקהב  7.6.2022.  ב רחסמה-

  אל התע דע יכ הדבועה לשב רקיעב תאזו   רחאל דבלב םימי העברא.  רדגוה עוריאה ןולחעוריאה

  .הקידבה יאצממ אולמ ומסרופ

  "ךרעה וק" ןיבל "ריחמה וק" ןיב רעפה תא קודבל שי עוריאה תובקעב קזנה תא רחמתל תנמ לע

   טפשמה תיב ידי לע עבקנש יפכ , תודוא עדימה םוסרפ רחאל קר ושגפנעוריאה:ןוילעהש

  "יתימאה ךרעה" תא גציימה יטתופיה וק ונה ,(" line") "ךרע וק" הנוכמה ,ןושארה וקה"value

 ףקשמ אוהו ,ויוליג דעומ ןיבל העטמה עדימה םוסרפ ןיבש הפוקתה ךלהמב םוי לכב הינמה לש

  םדיב היה וליא הרחסנ וב םוי לכב הינמה רובע םלשל םינכומ םישכורה ויה ותוא  ריחמה תא

  ,("  line")  "ריחמה  וק"  הנוכמה  ,ינשה  וקה  .ורושאל  הרבחה  לש  הבצמל  עגונה  עדימהprice

  קספל  הקסיפב לאידע טפושה 'בכ)87  "םירומאה םידעומה לכב לעופב הינמה ריחמ תא ראתמ

  ש 'נ טרכיירשמ.("  א"ע345/03 ב ןידה

  

  היהש דשח תורמל)   עדימ  לוכיבכבהעטמ  הז הרקמב םיקסוע ונא ןיאש תורמל יכ ןייצנ הז רשקהב

  ךרעה וק ,(םישחרתמש םיעוריאהו לוהינה תוכיא ,חוקיפה יא ןיינעל עדימ לע בר ןמז ךשמב עודי

  וקו הרבחה תיינמ יוושב רחמותמ םיעוריאה לע עדימהשכ הרבחה  תיינמ  לש יוושה וניה הז הרקמב

  םייוקילה לע ,הפוקב םירסוחה לע רוביצל עודי היה אל רשאכ לעופב הרבחה תוינמ יווש וניה ריחמה

   .הרבחהמ ןידכ אלש םיפסכ לטנ ל"כנמהש ךכ לעו תימינפה הרקבב

   

   

   

  

   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 9 -  

 

  study -Event market model קושה לדומ תועצמאב עוריא רקח  .5

 

  ,  א"ת דדמ125 םייטנוולר סוחיי ידדמ רפסמ ונחבש רחאל , עוציב ךרוצל)  :הקידבהסוחייה דדמ 5.1.

  דדמה וניה םיסנניפ חוטיב  לת דדמ יכ ונאצמ ,(ביבא א"תםיסנניפ דדמ , חוטיב א"ת דדמםיסנניפו

  .לדומה תדימאל רתויב םיאתמה

  השולש םניהש  2021,   לש ןושארה ןועברה  לש  הדימא תפוקתב שמתשהל ונרחב  :הדימאה תפוקת 5.2.

  ךלהמב עדימה תגילז לש תורשפא ןוחבל תנמ לע עוריאה ינפל  שדוח לש רעפ םע רחסמ ישדוחםיי

  .עוריאה םורטש םיישדוחה

  רפסמ לע ףאו םימי רפסמ לע תוסרפתמ   ך םייתוהמ םיעוריא לש תועפשה :ללכעוריאה ןולחרדב 5.3.

  .חווידה רחאלש רסחמ  ימי   ךרואל ונקדב קזנה תאהעברא תועובש.

    ףיעס  האר)2.11    ךיראתמ  חווידה  תרגסמב2.6.2022  הטילשה  ילעב  תעדוה  יכ  ןייצנ הז  רשקהב

  המצמצ וז העדוה ,רמולכ .קזנה תכרעה תא םצמצש ןפואב עוריאה ןולח תא המהיז (וז תעד תווחל

  לע .רצונש ילכלכה קזנב תופשל םיבייחתמ םילעבהש ךכב ומצע ילילשה עוריאהמ רישיה קזנה תא

  הידעלבש רתויב תינרמש הכרעה הניה הז םוהיז לש רוחמת אלל עוריאה ןולחב קזנה תדימא ,ןכ

  .רתוי הובג תויהל היה יופצ הז יופיש אלל הרבחב תולהנתהה תובקעב דמאנה קזנה

  ב תמייתסמ הניאש תכשמתמ העפשהב ונתעדל רבודמ ל"נה הרקמבהעברא  :"עוריא טסופ" ןולח 5.4.

  תביתכ תעב הקידבל ןתינ וניא  םימי,  90   ל-  20   ענ כ"דבש  ע ו ר יאה טסופ ןולחןיב  .םידדוב רחסמ ימי

  .וז תעד תווח

  דמאנה לדומה תאצות 5.5.

   :דמאנה לדומה תואצות תא תראתמה הלבט ןלהל







  




   
  

  לדומל סחיב  רחאל הינמה יעוציב חותינחווידה . 6

  הרבחה תיינמ לע קושה תעפשה לש לורטנ םיעצבמ ונא ,עוריאה םורט ונדמא םתוא םילדומה תועצמאב,

  האצותכ העפשהה לדוג השעמל  אוה   , הינמה יעוציב ןיבל דמאנה לדומה ןיב  רעפה .לעופב  רחאלחווידה

  םישרפהה  יכ  t ןחבמ  תועצמאב  םיאדוומ  ונא  .רומא  חווידב  םיעיקשמה  רוביצל  הלגתהש  עוריאהמ

  דמאנה לדומהמ קהבומ ןפואב םינוש עוריאה רחאל םירבטצמה.

   

  

  

  

  
   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 10 -  

 

   חווידה תובקעב קזנה רועיש תדימא  ןלהל

  עיגמו עוריאה רחאל    םויהמ לחה קהבומןושארה  לדומהמ רבטצמה רעפה ,ונדמא ותוא לדומה יפ לע

  ר ב טצמ   רועישב הרבחה תיינמ רעשב  העיגפל  לדומה יפ לע,  ליבוה,    .עוריאה(!)    ל ש   תוקהבומ תמרל100%

   .עוריאה רחאלש םימיה תעבראב 25.4% כ לש-

   .25.4%  לש רועישב  ותוא תמכמו קזנה םויק תא טלחומ ןפואב חיכומ לדומה

   קזנה תדימא

  תמר  רבטצמ רעפ
  תוקהבומt-stat    ןקת תייטס   לדומהמ   לדומהמ רעפ  ךיראת עוריאהמ םימי
    18.04% -0.23 3.96% -0.91% -1.08% 29/05/2022 -3 
      4.23% 0.05 3.24% 0.17% -0.03% 30/05/2022 -2 
      6.94% 0.09 2.29% 0.20% 0.20% 31/05/2022 -1 

    100.00% -10.18 2.29% -23.31% -23.31% 01/06/2022 1 
    100.00% -6.45 3.24% -20.87% 3.18% 02/06/2022 2 
    100.00% -5.71 3.96% -22.65% -2.25% 06/06/2022 3 
    100.00% -5.55 4.58% -25.42% -3.59% 07/06/2022 4 

   

   -כב   דרי  הרבחה תיינמ   רעש  עוריאל םיבקועה רחסמה  ימי תעבראב    תובקעבש איה ונתנקסמ,עוריאה

   תעפשה לורטנב. תאזוקושה 25.42%

  רומאהםי.    ן י ב ל הרבחה תיינמעוריאהםי  ר ע שב הדיריה  ן י ב   רישי  י ת ביס  ר ש ק ונשי יכ    ו ז   הקידבהחיכומ

   הצובקל קזנה תכרעהתגצוימה 7.

  םינמנ םניאש הטילשה ילעב תפסותב רוביצה ברקמ תוינמ ילעב ללכ ,תגצוימה הצובקה תרדגהל םאתהב

    .הרבחה תוינממ  לש רועישב םיקיזחמ הטילשה ןיערג לע34.37%

    ךרעומ קזנה רועישוכב-    םויב רחסמה תריגסל ןוכנ ₪31.5.2022  ןוילימ    לע דמע58.53    תרבח יוושטנוי

   .₪  ןוילימ  5.1   כ  לע  דמוע  תגצוימה  הצובקה  ללכל  קזנה  יכ  אצוי  ךכמ-  ,הרבחה  יוושמ  25.42%

   

   

       

       

       

     

  

  תשקבמל קזנה תכרעה 8.

  לע דמאנ הינמל קזנה  .הרבחה תוינמ לש .נ.ע  100   -ב הקיזחמ ,ןידה יכרוע י"ע יל רסמנש יפכ ,תשקבמה

  .₪  226.52 כב דמאנ תשקבמל-  ללוכה   ךכיפל ו הינמל תורוגאקזנה  226.52 ב ונתכרעה יפ-

  

  

  

   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

  - 11 -  

 

  

 תורוקמ  .9

  .ה"יאמ רתא ךותמ םייפסכ תוחודו תועדוה 9.1.

  דגנכ תיגוציי העיבת רושיאל השקבה.  תטויטהרבחה 9.2.

  .ע"ינל הסרובה לש םיימשר םינותנ 9.3.

  .הדובעה ףוגב םיטטוצמה םירקחמו םירמאמ 9.4.

  9.5.

 
 בתוכה לש ןויסינו הלכשה תיצמת 10.
  
  :הלכשה

  .ןוירוג ןב תטיסרבינואמ םיקסע  להנמו הלכלכב ןושאר ראות 

  .ןוירוג ןב תטיסרבינואמ םינייטצמ לולסמב ןומימב תוחמתה םע הלכלכב ינש ראות 

  :יעוצקמ ןויסינ

  ןוה  לוהינו  הזילנא  ,יסנניפ  ץועיי  יתוריש  תנתונ רשא  "  םיסנניפ  ורקאמ"  לש  םילעבו  ל"כנממ"עב 

 .תוילכלכ תעד תווחו םידיגאתל

  .תונידמו תורבח לש ןוכיס תוימרפו יארשא יגוריד םוחתב םיימדקא םירקחמ 

  .ןוהה קושב ןויסינ םינש  לעמ14 

  היסנפה תונרק    ם י תימע'ו םיסנניפ הרונמ :םהיניב ,לארשיב םילודגה םיידסומה םיפוגב תועקשה להנמ- 

  .'תוקיתווה

 .םיתימעב למגה תופוק לש ח"גאה קית להנמ היה ריכשכ ןורחאה ודיקפתב 

  ושמיש רשא ,טועימה תוינמ ילעב לש םטבמ תדוקנמ ,'םיתימע' רובע תובר תוימינפ  תעד תווח תביתכ 

   .'םיתימע'ב תוטלחה תלבקל ןגועכ

   םיסנניפל הימדקאבBDO. הצרמ 

  .תויגוציי תועיבת תרגסמב  Study לדומ תועצמאב קזנה תכרעה םוחתב תובר תעד תווח תביתכEvent 

 













   

  Gilad@MacroFC.com לא ו ד"      073-7372228  ן ו פ ל ט:      :050-9934569ד י י נ          ה מ ו ק9 ,ק ר ב ינב-  אבכוכ רב16 ,םיסנניפ ורקאמ

 "

# Define a regular expression pattern to match Hebrew words
hebrew_pattern = re.compile(u"[\u0590-\u05fe]+")

# Find all matches of the pattern in the text and reverse the order of the Hebrew words
reversed_hebrew_words = [word[::-1] for word in hebrew_pattern.findall(text)]

# Replace the original Hebrew words in the text with the reversed words
for word in reversed_hebrew_words:
    text = text.replace(word[::-1], word)

# Print the updated text
print(text)

