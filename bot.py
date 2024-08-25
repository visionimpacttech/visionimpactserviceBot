
from telethon import TelegramClient, events, Button

API_ID = '25003519'
API_HASH = '36f2224113d4ddc3808ba8e849da7e71'
BOT_TOKEN = '7520828607:AAEy3990R79GycuGhVd4N0inCRfxhpypJgo'

client = TelegramClient('Visionimpact_serviceBot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Start command with CTA buttons
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "Welcome to Vision Impact AI-powered Film Solutions! Click on any of the options below to get started.",
        buttons=[
            [Button.inline("Explore Our Services", b"explore_services")],
            [Button.inline("Film Boost", b"film_boost"), Button.inline("Book a Consultation", b"book_consultation")],
            [Button.inline("View Portfolio", b"view_portfolio")],
            [Button.inline("Learn More About AI in Film", b"learn_more")],
            [Button.inline("Join Our Community", b"join_community")],
            [Button.inline("Contact Us", b"contact_us"), Button.inline("Start Learning with AI Technologies", b"start_learning")],
            [Button.inline("FAQs", b"view_faqs")]
        ]
    )
    raise events.StopPropagation

# Callback for "Explore Our Services"
@client.on(events.CallbackQuery(data=b"explore_services"))
async def explore_services(event):
    await event.edit(
        "Discover our cutting-edge AI solutions for film production. Choose a service to learn more.",
        buttons=[
            [Button.inline("Storyboard Creation", b"storyboard_creation")],
            [Button.inline("AI Scriptwriting", b"ai_scriptwriting")],
            [Button.inline("Pre-Visualization", b"pre_visualization")],
            [Button.inline("Moodboard & Design", b"moodboard_design")],
            [Button.inline("Back to Main Menu", b"back_to_menu")]
        ]
    )

@client.on(events.CallbackQuery(data=b"storyboard_creation"))
async def storyboard_creation(event):
    await event.edit("Explore Storyboard Creation here: https://drive.google.com/file/d/1ZHQQkpofSkSe-Mqt6djv0JNFQvBmSeF7/view?usp=sharing",
                     buttons=[Button.inline("Back to Services", b"explore_services")])

@client.on(events.CallbackQuery(data=b"ai_scriptwriting"))
async def ai_scriptwriting(event):
    await event.edit("Explore AI Scriptwriting here: https://drive.google.com/file/d/1ZHQQkpofSkSe-Mqt6djv0JNFQvBmSeF7/view?usp=sharing",
                     buttons=[Button.inline("Back to Services", b"explore_services")])

@client.on(events.CallbackQuery(data=b"pre_visualization"))
async def pre_visualization(event):
    await event.edit("Explore Pre-Visualization here: https://drive.google.com/file/d/1ZHQQkpofSkSe-Mqt6djv0JNFQvBmSeF7/view?usp=sharing",
                     buttons=[Button.inline("Back to Services", b"explore_services")])

@client.on(events.CallbackQuery(data=b"moodboard_design"))
async def moodboard_design(event):
    await event.edit("Explore Moodboard & Character Design here: https://drive.google.com/file/d/1ZHQQkpofSkSe-Mqt6djv0JNFQvBmSeF7/view?usp=sharing",
                     buttons=[Button.inline("Back to Services", b"explore_services")])

# Callback for "Film Boost"
@client.on(events.CallbackQuery(data=b"film_boost"))
async def film_boost(event):
    await event.edit("Interested in our services? Get a personalized quote by sharing your project details with us: https://forms.gle/YZ3udBEN95QHAvgs9",
                     buttons=[Button.inline("Back to Main Menu", b"back_to_menu")])

# Callback for "Book a Consultation"
@client.on(events.CallbackQuery(data=b"book_consultation"))
async def book_consultation(event):
    await event.edit("Schedule a discovery call with us here: https://calendly.com/visionimpacttechnologies",
                     buttons=[Button.inline("Back to Main Menu", b"back_to_menu")])

# Callback for "View Portfolio"
@client.on(events.CallbackQuery(data=b"view_portfolio"))
async def view_portfolio(event):
    await event.edit("Check out our previous projects and see how we’ve helped filmmakers achieve their vision. Read more at: https://attempt-be.unicornplatform.page/oofi-media-ai-powered-film-solutions/",
                     buttons=[Button.inline("Back to Main Menu", b"back_to_menu")])

# Callback for "Learn More About AI in Film"
@client.on(events.CallbackQuery(data=b"learn_more"))
async def learn_more(event):
    await event.edit("Explore how AI is transforming the film industry: https://drive.google.com/file/d/1ZHQQkpofSkSe-Mqt6djv0JNFQvBmSeF7/view?usp=sharing",
                     buttons=[Button.inline("Back to Main Menu", b"back_to_menu")])

# Callback for "Join Our Community"
@client.on(events.CallbackQuery(data=b"join_community"))
async def join_community(event):
    await event.edit("Be a part of our creative community. Get updates, tips, and more delivered to your inbox. https://chat.whatsapp.com/K6iMxmW98Zj7XHnpSYgvxH",
                     buttons=[Button.inline("Back to Main Menu", b"back_to_menu")])

# Callback for "Contact Us"
@client.on(events.CallbackQuery(data=b"contact_us"))
async def contact_us(event):
    await event.edit("Have questions? We're here to help! Contact us via email or phone.",
                     buttons=[
                         [Button.inline("Email Us", b"email_us")],
                         [Button.inline("Call Us", b"call_us")],
                         [Button.inline("Back to Main Menu", b"back_to_menu")]
                     ])

@client.on(events.CallbackQuery(data=b"email_us"))
async def email_us(event):
    await event.edit("You can reach us at: visionimpacttechnologies@gmail.com",
                     buttons=[Button.inline("Back to Contact", b"contact_us")])

@client.on(events.CallbackQuery(data=b"call_us"))
async def call_us(event):
    await event.edit("You can call us at: +91 9606989902",
                     buttons=[Button.inline("Back to Contact", b"contact_us")])

# Callback for "Start Learning with AI Technologies"
@client.on(events.CallbackQuery(data=b"start_learning"))
async def get_started(event):
    await event.edit(
        "Ready to start your journey with AI technologies? https://shorturl.at/I8AiU",
        buttons=[
            Button.inline("Back to Main Menu", b"back_to_menu")]
        
    )

# Callback for "View FAQs"
@client.on(events.CallbackQuery(data=b"view_faqs"))
async def view_faqs(event):
    await event.edit(
        "Frequently Asked Questions:\n\n"
        "1. **What services does Vision Impact offer?**\n"
        "   Vision Impact offers AI-powered solutions for filmmakers, including Storyboard Creation, AI Scriptwriting, Pre-Visualization, and more.\n\n"
        "2. **How can AI help in film production?**\n"
        "   AI streamlines processes like scriptwriting, storyboard creation, and visual effects, allowing filmmakers to focus on creativity.\n\n"
        "3. **How do I book a consultation with Vision Impact?**\n"
        "   Click on 'Book a Consultation' in the bot to schedule a discovery call.\n\n"
        "4. **Can I get a personalized quote for my film project?**\n"
        "   Yes, click on 'Film Boost' in the bot to get a customized quote.\n\n"
        "5. **What is Storyboard Creation?**\n"
        "   It is the process of visually planning your film’s scenes before production. Our AI tools help create detailed storyboards quickly.\n\n"
        "6. **How do I access the AI tools provided by Vision Impact?**\n"
        "   Click on 'Start Learning with AI Technologies' to explore our AI tools.\n\n"
        "7. **How can I view examples of Vision Impact’s previous work?**\n"
        "   Click on 'View Portfolio' to see our previous projects.\n\n"
        "8. **How do I join the Vision Impact community?**\n"
        "   Click on 'Join Our Community' to connect with other creatives and professionals.\n\n"
        "9. **What should I do if I have more questions or need support?**\n"
        "   Click on 'Contact Us' to reach out via email or phone.\n\n"
        "10. **Is there any way to learn more about AI’s role in the film industry?**\n"
        "   Click on 'Learn More About AI in Film' to explore articles and videos.",
        buttons=[Button.inline("Back to Main Menu", b"back_to_menu")]
    )

# Callback for "Back to Main Menu"
@client.on(events.CallbackQuery(data=b"back_to_menu"))
async def back_to_menu(event):
    await start(event)

# Add more callbacks for specific services or actions if needed

client.start()
print("Bot is running")
client.run_until_disconnected()

print("Bot has stopped")
