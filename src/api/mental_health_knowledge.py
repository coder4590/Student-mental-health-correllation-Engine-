# ============================================================
# MINDGUARD — MENTAL HEALTH KNOWLEDGE BASE
# ============================================================
# This file contains the complete therapeutic response library.
# Each entry has:
#   - patterns: list of phrases students might type
#   - response: detailed, empathetic, medically-informed answer


KNOWLEDGE_BASE = [

    # ============================================================
    # SECTION 1: DEPRESSION SYMPTOMS (CRITICAL CATEGORY)
    # ============================================================

    # --- Feeling Empty / Numb ---
    {
        "patterns": [
            "i feel empty", "i feel numb", "nothing matters", "i don't feel anything",
            "emotionally numb", "why am i so empty", "i feel hollow", "i feel dead inside",
            "no emotions", "i can't feel", "emptiness", "feeling void", "i am empty",
            "nothing feels real", "i feel nothing", "i am numb", "i've gone numb",
            "no feelings", "completely empty", "void inside", "emotional numbness",
            "i don't care about anything", "everything is meaningless", "what is the point",
            "life is meaningless", "i feel detached", "i feel disconnected",
            "feeling blank", "my mind is blank", "i feel flat", "no joy in anything",
            "i can't enjoy things", "nothing brings me joy", "i've lost interest",
            "things i used to love don't matter", "anhedonia"
        ],
        "response": (
            "I hear you, and I want you to understand something important: "
            "this feeling of emptiness is not your fault, and it is not permanent.\n\n"

            "**WHAT'S HAPPENING IN YOUR BRAIN:**\n"
            "Depression literally changes how your brain processes emotion. "
            "The neural circuits responsible for pleasure and motivation — "
            "particularly the dopamine and serotonin pathways — become underactive. "
            "This isn't a weakness or a character flaw. It's a measurable neurochemical "
            "state that millions of people experience. Your brain's emotional centers "
            "haven't disappeared — they've temporarily gone offline as a protective "
            "mechanism against overwhelming stress or trauma.\n\n"

            "**WHAT YOU CAN DO TODAY:**\n"
            "1. **Gentle stimulation**: Listen to music you used to love, even if it "
            "doesn't hit the same way right now. Your brain still registers it on some level.\n"
            "2. **Physical sensation**: Hold something warm (a cup of tea, a heating pad). "
            "Physical warmth can trigger small releases of oxytocin, the bonding hormone.\n"
            "3. **Nature exposure**: If you can, sit outside for 10 minutes. Natural light "
            "and green spaces have measurable antidepressant effects.\n"
            "4. **Micro-tasks**: Don't aim for productivity. Aim for one tiny thing: "
            "brush your teeth, open a window, drink a glass of water. Each completed "
            "micro-task sends a small signal to your brain that you still have agency.\n\n"

            "**WHEN TO SEEK PROFESSIONAL HELP:**\n"
            "If this emptiness has lasted more than two weeks, or if it's interfering "
            "with your ability to attend classes, maintain basic self-care, or connect "
            "with others, please speak with a mental health professional. Therapy — "
            "particularly CBT (Cognitive Behavioral Therapy) and behavioral activation — "
            "has strong evidence for treating exactly what you're describing.\n\n"

            "**YOU ARE STILL IN THERE.**\n"
            "The fact that you can recognize and describe this emptiness means you're "
            "still aware, still conscious, still fighting. The feelings will return "
            "gradually as your nervous system heals. This is not forever. You are not broken."
        )
    },

    # --- Feeling Worthless / Self-Hatred ---
    {
        "patterns": [
            "i feel worthless", "i hate myself", "i am useless", "why am i so worthless",
            "no one needs me", "i'm a burden", "i am not good enough", "i hate who i am",
            "i am a failure", "i can't do anything right", "i disgust myself",
            "i don't deserve happiness", "i deserve to suffer", "i am pathetic",
            "self hatred", "i loathe myself", "i'm a waste of space", "i ruin everything",
            "everyone would be better off without me", "i don't deserve love",
            "i'm stupid", "i'm ugly", "i'm worthless", "i am nothing",
            "no value", "i have no value", "i contribute nothing", "i'm inadequate",
            "i feel inferior", "i compare myself to others and fail", "imposter syndrome",
            "i don't belong here", "i'm a fraud", "everyone is better than me"
        ],
        "response": (
            "I need you to hear this clearly: **That voice telling you that you're "
            "worthless is a symptom of depression. It is not the truth.**\n\n"

            "**UNDERSTANDING THE 'INNER CRITIC':**\n"
            "Depression hijacks your brain's self-evaluation circuits. The prefrontal "
            "cortex, which normally balances negative thoughts with perspective, becomes "
            "underactive during depression. Meanwhile, the amygdala — your brain's fear "
            "center — becomes overactive. The result? Your brain generates negative "
            "self-judgments constantly, and the part that would normally say 'that's "
            "not true' is too depleted to push back. This is a neurochemical imbalance, "
            "not an accurate self-assessment.\n\n"

            "**PRACTICAL STEPS TO CHALLENGE THESE THOUGHTS:**\n"
            "1. **Name the voice**: Give your inner critic a name separate from yourself — "
            "'Brian the Bully' or 'The Depression Demon.' When those thoughts come, "
            "say: 'That's Brian talking again, not reality.'\n"
            "2. **Evidence challenge**: When you think 'I'm a failure,' write down 3 "
            "objective pieces of evidence against that statement. You're in university "
            "— you've already succeeded more than you realize.\n"
            "3. **The friend test**: Would you say these things to a friend who was "
            "suffering? If not, why are you saying them to yourself?\n"
            "4. **Values clarification**: Your worth is not measured by productivity, "
            "grades, relationships, or other people's opinions. You have inherent value "
            "simply because you exist.\n\n"

            "**YOU ARE NOT YOUR THOUGHTS.**\n"
            "Thoughts are mental events, not facts. Depression generates thousands of "
            "negative thoughts daily — they feel true because they're loud and frequent, "
            "not because they're accurate. Cognitive Behavioral Therapy (CBT) is "
            "specifically designed to help you separate from these thoughts and evaluate "
            "them objectively. Consider reaching out to a therapist who specializes in CBT.\n\n"

            "**REMEMBER:**\n"
            "The most successful people in the world have failed more times than you've "
            "tried. Your worth as a human being has never been, and will never be, "
            "determined by your achievements or other people's opinions. You are enough. "
            "Right now. Exactly as you are."
        )
    },

    # --- Hopelessness ---
    {
        "patterns": [
            "i feel hopeless", "there's no way out", "things will never get better",
            "i have no future", "nothing will change", "what's the point of trying",
            "it's too late for me", "i'm beyond help", "no hope", "hopeless",
            "this will never end", "i'm stuck like this forever", "no way out",
            "there is no light", "i can't see a future", "my future is dark",
            "nothing to look forward to", "why bother", "it won't get better",
            "i've tried everything", "nothing works", "i give up", "beyond repair"
        ],
        "response": (
            "**HOPELESSNESS IS DEPRESSION'S MOST EFFECTIVE LIE.**\n\n"

            "Here's a medical fact that depression desperately doesn't want you to know: "
            "**Every single depressive episode ends.** Every single one. The human brain "
            "cannot sustain that level of distress permanently. The hopelessness you "
            "feel right now is not a prediction — it's a symptom.\n\n"

            "**WHY YOUR BRAIN LIES ABOUT THE FUTURE:**\n"
            "Depression depletes the neurotransmitters needed for future-oriented "
            "thinking. Specifically, serotonin and norepinephrine are critical for "
            "imagining positive future scenarios. When they're low, your brain literally "
            "cannot access positive predictions. It's like trying to see color in a "
            "dark room — the colors exist, but you don't have the light to see them. "
            "Treatment restores that light.\n\n"

            "**THE EVIDENCE YOU CAN'T SEE RIGHT NOW:**\n"
            "- Depression treatments (therapy, medication, lifestyle changes) have "
            "60-80% effectiveness rates.\n"
            "- The vast majority of people who experience a major depressive episode "
            "recover completely.\n"
            "- Many report that the experience, while painful, eventually led to deeper "
            "self-understanding and resilience.\n\n"

            "**WHAT TO DO WHEN HOPE FEELS IMPOSSIBLE:**\n"
            "1. **Borrow hope from others**: When you can't generate your own hope, "
            "let others hold it for you. Call a friend who believes in you. Read "
            "recovery stories online.\n"
            "2. **Trust the process, not your feelings**: Your feelings say 'nothing "
            "will work.' Science says treatment works. Trust the data.\n"
            "3. **One hour at a time**: Don't try to imagine a better future. Just "
            "get through this hour. Then the next.\n"
            "4. **Professional help works**: If you haven't tried therapy or medication, "
            "you haven't tried everything. There are dozens of treatment approaches.\n\n"

            "**THIS IS TEMPORARY.**\n"
            "Depression is episodic by nature. It ends. Your future self exists, and "
            "they will look back on this period with compassion for what you survived. "
            "Keep going. One hour. One day. The light returns."
        )
    },

    # --- Crying / Sadness ---
    {
        "patterns": [
            "i can't stop crying", "i cry all the time", "crying for no reason",
            "i feel so sad", "overwhelming sadness", "i'm so sad", "constant sadness",
            "why am i so sad", "i cry myself to sleep", "tears", "sobbing",
            "i cry every night", "i cried today", "nonstop crying", "uncontrollable crying",
            "i feel like crying", "i want to cry but i can't", "i can't even cry anymore",
            "sad all the time", "i feel miserable", "deep sadness", "my heart hurts",
            "emotional pain", "i'm hurting", "i am in pain"
        ],
        "response": (
            "Crying is not a sign of weakness — it's your body's natural pressure "
            "release valve. When emotional pressure builds up, tears release stress "
            "hormones like cortisol, literally flushing them out of your system.\n\n"

            "**WHY YOU'RE CRYING SO MUCH:**\n"
            "Depression lowers your emotional regulation threshold. Your brain's "
            "ability to modulate emotional responses is compromised, so stimuli "
            "that would normally cause mild sadness instead trigger overwhelming "
            "emotional releases. This is a neurological symptom, not a personality flaw.\n\n"

            "**IF YOU'RE CRYING CONSTANTLY:**\n"
            "- Let it happen. Fighting tears increases internal stress.\n"
            "- After crying, drink water and rest. Crying is physically exhausting.\n"
            "- Track if there's a pattern (certain times of day, certain triggers).\n"
            "- If crying interferes with daily functioning for more than 2 weeks, "
            "speak with a professional.\n\n"

            "**IF YOU CAN'T CRY ANYMORE:**\n"
            "The inability to cry despite wanting to is also a depression symptom — "
            "emotional numbness. Your brain has shut down the crying response to "
            "protect you from overwhelm. This too will pass with treatment.\n\n"

            "Your tears are not your enemy. They're evidence that you're still "
            "feeling, still processing, still human."
        )
    },

    # --- Can't Get Out of Bed / Fatigue ---
    {
        "patterns": [
            "i can't get out of bed", "i don't want to wake up", "i sleep all day",
            "getting out of bed is hard", "no energy to get up", "i just want to sleep",
            "tired all the time", "exhausted", "no energy", "fatigue",
            "i'm always tired", "why am i so tired", "i have no motivation",
            "i don't want to do anything", "i can't move", "i feel heavy",
            "my body feels heavy", "lethargic", "no willpower", "bedridden",
            "i want to stay in bed forever", "can't face the day", "dreading today"
        ],
        "response": (
            "**THIS IS NOT LAZINESS. THIS IS PSYCHOMOTOR RETARDATION — A REAL MEDICAL SYMPTOM.**\n\n"

            "In depression, your nervous system slows down physically. Your muscles "
            "feel heavy, your reaction times slow, and every movement requires "
            "enormous effort. This is measurable on brain scans and has nothing "
            "to do with willpower or character.\n\n"

            "**THE MICRO-STEP METHOD:**\n"
            "Don't try to 'get up and be productive.' Break 'getting up' into the "
            "smallest possible steps:\n"
            "  Step 1: Open your eyes.\n"
            "  Step 2: Sit up in bed.\n"
            "  Step 3: Put feet on the floor.\n"
            "  Step 4: Stand up.\n"
            "  Step 5: Walk to bathroom.\n"
            "Celebrate each step. If today you only opened your eyes and sat up, "
            "**that counts as progress.**\n\n"

            "**PRACTICAL TIPS:**\n"
            "1. Place water and a snack by your bed before sleeping.\n"
            "2. Set a gentle alarm across the room so you have to stand to turn it off.\n"
            "3. Open curtains immediately — natural light signals wakefulness.\n"
            "4. Don't judge your morning self by your evening self's expectations.\n\n"

            "If this fatigue persists for weeks despite adequate rest, see a doctor. "
            "Depression-related fatigue can also have physical causes (thyroid, "
            "vitamin deficiencies, anemia) that are treatable."
        )
    },

    # --- No Motivation / Anhedonia ---
    {
        "patterns": [
            "no motivation", "i don't enjoy anything anymore", "things i loved don't interest me",
            "no pleasure", "i feel nothing when i do things", "anhedonia",
            "lost interest in hobbies", "why can't i enjoy things",
            "i used to love this and now i don't care", "lost passion",
            "nothing excites me", "i don't look forward to anything",
            "can't feel happiness", "joyless", "no enjoyment",
            "everything feels pointless", "why bother doing anything if i feel nothing"
        ],
        "response": (
            "**ANHEDONIA** — the inability to feel pleasure — is one of depression's "
            "core symptoms. Your brain's reward system isn't broken; it's depleted.\n\n"

            "**WHY THIS HAPPENS:**\n"
            "Dopamine — the neurotransmitter responsible for anticipation of reward "
            "and experience of pleasure — becomes dysregulated in depression. Things "
            "that would normally trigger a dopamine release no longer register. This "
            "is not permanent damage. Dopamine pathways can heal and regenerate.\n\n"

            "**THE 'DO IT ANYWAY' PRINCIPLE:**\n"
            "Behavioral activation therapy has strong evidence for treating anhedonia. "
            "The principle: **action comes before motivation, not after.** Do the "
            "activity even though you feel nothing. Your brain registers the action "
            "and slowly rewires the reward pathway. It takes time — weeks, not days.\n\n"

            "**START HERE:**\n"
            "1. Pick one activity you used to enjoy.\n"
            "2. Do it for 10 minutes without expecting to feel anything.\n"
            "3. Just notice what you notice. No judgment.\n"
            "4. Repeat daily. The feelings will return gradually.\n\n"

            "This is hard work. It's like physical therapy for your brain. But the "
            "research is clear: behavioral activation is as effective as medication "
            "for mild to moderate depression."
        )
    },

    # --- Overwhelm / Can't Cope ---
    {
        "patterns": [
            "i'm overwhelmed", "i can't cope", "everything is too much", "i'm drowning",
            "too much pressure", "i can't handle this", "i'm breaking down",
            "mental breakdown", "i'm falling apart", "i'm losing control",
            "i can't manage", "it's all too much", "overwhelmed by everything",
            "i feel like i'm going crazy", "snapping", "can't take it anymore",
            "at my breaking point", "on the edge", "losing my mind",
            "can't function", "barely holding on", "life is overwhelming"
        ],
        "response": (
            "When everything feels overwhelming, your nervous system is in a state "
            "called **hyperarousal** — it's perceiving everything as a threat, even "
            "small tasks. This is exhausting and it's not your fault.\n\n"

            "**IMMEDIATE GROUNDING EXERCISE:**\n"
            "Right now, wherever you are:\n"
            "1. Name 5 things you can SEE (look around, name them out loud)\n"
            "2. Name 4 things you can TOUCH (your clothes, your chair, your skin)\n"
            "3. Name 3 things you can HEAR (traffic, clock, breathing)\n"
            "4. Name 2 things you can SMELL (coffee, air, fabric)\n"
            "5. Name 1 thing you can TASTE (or imagine a taste)\n\n"
            "This pulls your brain out of the threat-response and back to the "
            "present moment where, right now, you are safe.\n\n"

            "**SHRINK YOUR WORLD:**\n"
            "When everything is too much, don't try to handle everything. Handle "
            "only the next 5 minutes. Then the next 5. Your only job right now "
            "is breathing and staying alive. Everything else can wait.\n\n"

            "If you're in Bangladesh, Kaan Pete Roi offers free emotional support: "
            "01779554391 / 01779554392. If you're elsewhere, please reach out to "
            "a local crisis line. You deserve support."
        )
    },

    # ============================================================
    # SECTION 2: SUICIDAL THOUGHTS & CRISIS (CRITICAL CATEGORY)
    # ============================================================

    # --- Active Suicidal Ideation ---
    {
        "patterns": [
            "i want to die", "i want to end it", "i want to kill myself",
            "suicide", "kms", "end my life", "better off dead",
            "not want to live anymore", "kill myself", "i should just die",
            "i'm going to kill myself", "planning to end my life",
            "i have a plan", "i know how i would do it", "suicidal",
            "i want to disappear", "i want to cease to exist",
            "take my own life", "end it all", "i'm done",
            "i can't do this anymore", "i want out",
            "i don't want to be alive", "let me die", "wish i was dead",
            "wish i never existed", "never been born"
        ],
        "response": (
            "**PLEASE STOP AND READ THIS CAREFULLY.**\n\n"

            "What you're experiencing right now is a **medical emergency.** "
            "These thoughts are a symptom of severe depression — they are your "
            "brain sending a critical distress signal, not a rational conclusion.\n\n"

            "**PLEASE DO ONE OF THESE RIGHT NOW:**\n"
            "1. Call the **National Mental Health Helpline: 999** (if in Bangladesh).\n"
            "2. Call **Kaan Pete Roi: 01779554391 or 01779554392** — they speak "
            "Bangla and English and are trained to help.\n"
            "3. Go to the nearest hospital emergency room and tell them you're "
            "having thoughts of suicide.\n"
            "4. Call a trusted friend or family member and tell them exactly what "
            "you're thinking. Don't protect them from this information.\n"
            "5. If you're outside Bangladesh: call or text your local crisis "
            "helpline immediately.\n\n"

            "**WHY YOUR BRAIN IS LYING TO YOU RIGHT NOW:**\n"
            "Depression creates cognitive constriction — a tunnel vision where "
            "your brain literally cannot access memories of ever feeling better "
            "or imagine a future where things improve. This is a temporary "
            "neurochemical state. It feels permanent, but it's not. Every "
            "depressive episode ends, including this one.\n\n"

            "**THE FACTS:**\n"
            "- The vast majority of people who survive suicidal crises do not "
            "go on to die by suicide.\n"
            "- The intense desire to die typically passes within hours to days "
            "with proper support.\n"
            "- Treatment works. Therapy and medication save lives.\n\n"

            "**YOU MATTER.**\n"
            "Your death would create a permanent wound in the lives of everyone "
            "who knows you — whether you believe that right now or not. The "
            "depression is lying to you about your value and your future. "
            "Please stay. Please reach out. You are not alone."
        )
    },

    # --- Passive Suicidal Ideation ---
    {
        "patterns": [
            "i wish i wouldn't wake up", "i hope i don't wake up tomorrow",
            "i wouldn't mind if i died", "if a car hit me i wouldn't care",
            "i don't want to die but i don't want to live", "passive suicidal",
            "i'm tired of living", "living is exhausting", "why am i still alive",
            "i'm just existing not living", "i'm waiting to die",
            "no will to live", "lost the will to live",
            "what's keeping me alive", "i don't see the point",
            "living is too hard", "i wish it would all just end",
            "i wish i could just sleep forever", "never wake up"
        ],
        "response": (
            "**PASSIVE SUICIDAL IDEATION IS STILL SERIOUS.**\n\n"

            "You may not have an active plan, but wishing you wouldn't wake up "
            "or wouldn't mind dying is a major warning sign. This is your mind "
            "telling you that your current level of suffering has become "
            "unbearable — and you deserve help reducing that suffering.\n\n"

            "**THE DIFFERENCE BETWEEN ACTIVE AND PASSIVE:**\n"
            "- Active: 'I plan to end my life.'\n"
            "- Passive: 'I wouldn't mind if I didn't wake up.'\n"
            "Both require immediate professional attention. Passive ideation "
            "often precedes active ideation.\n\n"

            "**WHAT TO DO TODAY:**\n"
            "1. Make an appointment with a mental health professional this week.\n"
            "2. Tell someone you trust: 'I've been having thoughts about not "
            "wanting to be alive. I need support.'\n"
            "3. Remove or secure any means of self-harm in your environment.\n"
            "4. Create a safety plan: list people to call, places to go, "
            "activities that distract you when these thoughts intensify.\n\n"

            "**YOU DESERVE TO FEEL BETTER.**\n"
            "The fact that a part of you is still reaching out — even passively — "
            "means there's still hope. Let professionals help you carry this weight. "
            "You don't have to carry it alone."
        )
    },

    # --- Self-Harm Urges ---
    {
        "patterns": [
            "i want to hurt myself", "i want to self harm", "cut myself", "cutting",
            "self injury", "selfharm", "self harm urges", "i feel like cutting",
            "i need to hurt myself", "relapsing on self harm",
            "i want to feel pain", "the urge to cut", "fighting the urge to self harm",
            "burning myself", "hitting myself", "i hurt myself to feel something"
        ],
        "response": (
            "**SELF-HARM URGES ARE A COPING MECHANISM — AND THERE ARE SAFER ALTERNATIVES.**\n\n"

            "Self-harm often serves a function: it temporarily distracts from "
            "overwhelming emotional pain by creating physical sensation. But there "
            "are other ways to achieve that same relief without causing harm.\n\n"

            "**ALTERNATIVES TO TRY RIGHT NOW (DBT-BASED):**\n"
            "1. **Intense sensation**: Hold ice cubes in your hands. The intense "
            "cold provides similar sensory input without injury.\n"
            "2. **Snap a rubber band**: Wear a rubber band on your wrist and snap "
            "it when the urge comes.\n"
            "3. **Cold shower**: Brief cold exposure shocks your nervous system.\n"
            "4. **Red marker**: Draw on your skin where you want to cut. The "
            "visual can satisfy part of the urge.\n"
            "5. **Intense exercise**: Run, do pushups, anything that creates "
            "physical sensation.\n"
            "6. **Scream into a pillow**: Release the emotional pressure vocally.\n\n"

            "**SEEK PROFESSIONAL HELP:**\n"
            "DBT (Dialectical Behavior Therapy) was specifically developed for "
            "self-harm and has excellent outcomes. A therapist trained in DBT can "
            "help you build a toolkit of alternatives and address the underlying "
            "emotional pain driving the urges.\n\n"

            "These urges do not make you broken or crazy. They mean you're in pain "
            "and using the only tool that's worked so far. Let a professional help "
            "you build a bigger toolkit."
        )
    },

    # ============================================================
    # SECTION 3: FALLBACK, TYPOS, NONSENSE, AND INTELLIGENT RECOVERY
    # ============================================================

    # --- Random Characters / Nonsense ---
    {
        "patterns": [
            "asdf", "qwerty", "zxcv", "fdsa", "jkl", "hjkl",
            "aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff",
            "12345", "54321", "11111", "22222", "00000",
            "!!!", "???", "...", "....", ".....", ",,,,,",
            "bla bla", "blabla", "blah blah", "blahblah",
            "meh", "idk", "lol", "lmao", "bruh",
            "test", "testing", "hello world", "asdfghjkl",
            "qwertyuiop", "abcdefg", "hijklmnop"
        ],
        "response": (
            "It looks like you might have typed something randomly, or maybe "
            "your fingers slipped on the keyboard. That's completely okay.\n\n"

            "If you're struggling to put your feelings into words, that's "
            "actually quite common. Sometimes emotional pain is so big that "
            "words feel inadequate.\n\n"

            "Here are some prompts that might help you express what you're feeling:\n"
            "- 'I feel empty'\n"
            "- 'I can't stop crying'\n"
            "- 'I feel so alone'\n"
            "- 'I don't know what's wrong with me'\n"
            "- 'I need help'\n\n"

            "Take your time. There's no wrong way to reach out."
        )
    },

    # --- Typos / Misspellings ---
    {
        "patterns": [
            "helpp", "help meee", "hellp", "hepl", "halp",
            "sadd", "saaaad", "saddd", "depresed", "depresion",
            "deppression", "anxity", "anxcious", "anxiuos",
            "lonley", "lonlly", "lonli", "lonly",
            "wortless", "worthles", "worthess", "hopless", "hopeles",
            "crrying", "cryin", "cryng", "suicde", "sucid"
        ],
        "response": (
            "It looks like you might have made a small typo — that's totally "
            "fine, I can still understand what you're trying to say.\n\n"

            "From what I can tell, you're expressing that you're in pain or "
            "distress. Am I reading that correctly?\n\n"

            "If you can, try typing what you're feeling again in a slightly "
            "different way. Or you can use one of these common phrases:\n"
            "- 'I feel sad'\n"
            "- 'I feel anxious'\n"
            "- 'I feel alone'\n"
            "- 'I need help'\n"
            "- 'I don't know what to do'\n\n"

            "I'm here and I'm listening. Take your time."
        )
    },

    # --- Vague / Unsure ---
    {
        "patterns": [
            "i don't know", "idk", "not sure", "i'm not sure",
            "i don't know what's wrong", "i don't know how i feel",
            "unsure", "confused", "i don't understand",
            "what am i feeling", "i can't describe it",
            "i don't know what to say", "i have nothing to say",
            "nothing", "i don't know why i'm here"
        ],
        "response": (
            "Not knowing exactly what you're feeling is actually very common, "
            "especially when you're overwhelmed. Sometimes emotions are so big "
            "and tangled that they don't fit neatly into words like 'sad' or "
            "'anxious.'\n\n"

            "Here's what might help: instead of trying to name the emotion, "
            "try describing the physical sensations you're experiencing.\n\n"

            "- Do you feel a tightness in your chest?\n"
            "- Is there a heaviness in your body?\n"
            "- Are your thoughts racing or completely blank?\n"
            "- Do you feel like crying but can't?\n"
            "- Is there a lump in your throat?\n\n"

            "Physical sensations are often easier to identify than emotions, "
            "and they can give us clues about what's going on underneath.\n\n"

            "Take your time. Even just being here and reaching out is a step "
            "forward."
        )
    },

    # --- General Distress (Multiple Keywords) ---
    {
        "patterns": [
            "i'm struggling", "i'm having a hard time", "this is hard",
            "i can't do this", "it's too much", "i'm not okay",
            "i'm not doing well", "i feel terrible", "i feel awful",
            "this sucks", "life sucks", "my life is a mess",
            "everything is falling apart", "i'm a mess",
            "help me please", "please help", "somebody help",
            "i need someone", "i need to talk", "anyone there",
            "is anyone there", "can someone help", "i have no one to talk to"
        ],
        "response": (
            "I hear you. You're going through something really difficult right "
            "now, and the fact that you're reaching out — even just to a "
            "chatbot — shows strength, not weakness.\n\n"

            "**YOU'RE NOT ALONE.**\n"
            "There are people who want to help you, including people who have "
            "felt exactly what you're feeling right now.\n\n"

            "**HERE'S WHAT YOU CAN DO NEXT:**\n"
            "1. If you're in crisis: call a helpline or go to a hospital.\n"
            "2. If you need to talk: message a trusted friend. Just say 'I'm "
            "having a really hard time right now. Can we talk?'\n"
            "3. If you need professional help: contact your university's "
            "counseling center. They exist for exactly this purpose.\n"
            "4. If you just need to vent: keep typing. I'm here to listen.\n\n"

            "You've survived 100% of your worst days so far. You can survive "
            "this one too. One breath at a time."
        )
    },

    # --- Positive / Gratitude ---
    {
        "patterns": [
            "thank you", "thanks", "this helped", "i feel better",
            "good advice", "that makes sense", "i needed to hear that",
            "this was helpful", "you helped", "i appreciate this",
            "i'm grateful", "thankful", "thank u", "thx",
            "this is good", "helpful", "glad i talked", "feeling better now"
        ],
        "response": (
            "I'm really glad this conversation helped, even if just a little. "
            "You took the brave step of reaching out, and that's something to "
            "be proud of.\n\n"

            "**REMEMBER:**\n"
            "- Recovery isn't linear. There will be good days and hard days.\n"
            "- On the hard days, come back here. Talk again.\n"
            "- Keep building your support system — friends, family, counselors.\n"
            "- The fact that you felt better after talking proves that connection "
            "is powerful medicine for the mind.\n\n"

            "Keep going. You're doing better than you think you are."
        )
    },

    # --- ULTIMATE FALLBACK ---
    {
        "patterns": ["*"],
        "response": (
            "Thank you for sharing that with me. I want you to know that "
            "I hear you, and what you're describing sounds like it could be "
            "related to the emotional challenges that many university students "
            "face.\n\n"

            "Depression, anxiety, and stress manifest in many different ways — "
            "and what you're experiencing is real and valid. You are not making "
            "this up, and you are not 'overreacting.'\n\n"

            "**WHAT I RECOMMEND:**\n"
            "1. If you haven't yet, take the full mental health assessment. "
            "It will give you a more personalized analysis of your mental state.\n"
            "2. Reach out to your university's counseling services. They offer "
            "free, confidential support to students.\n"
            "3. If you're in crisis, contact a helpline immediately.\n"
            "4. Keep talking. Even to me. Connection is healing.\n\n"

            "You are not alone in this. Help is available, and recovery is "
            "possible. Keep reaching out."
        )
    }
]