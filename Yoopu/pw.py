from playwright import async_playwright
import asyncio


async def example():

    async with async_playwright() as asp:
        
        browser = await asp.chromium.launch(headless=False)

        url = "https://yoopu.me/view/b19eym10"

        page = await browser.newPage()

        await page.goto(url)


        await page.waitForSelector("//hexi-sheet")

        await page.addInitScript(source="alert('hello, world')")

        await page.addScriptTag(content='''
            document.getElementsByTagName("yp-slider-play")[0].style.display = "none";
            document.getElementsByClassName("fullscreen-button yoopu3-icon")[0].style.display = "none";
        ''')

        pu = await page.querySelector("//hexi-sheet")
        pu_all = await page.querySelectorAll("//hexi-sheet")

        print("pu:", pu)
        print("pu_all:", pu_all)

        pu_location = await pu.boundingBox()

        print("pu_location:", pu_location)

        instrument = await pu.getAttribute("instrument")

        print("instrument:", instrument)

        innerhtml = await pu.innerHTML()
        innertext = await pu.innerText()

        print("innerHtml:", innerhtml[:50])
        print("innerText:", innertext[:50])


        q = await page.querySelector("//form[@class='searchContainer']/input")
        yoopu3_icon = await page.querySelector("//form[@class='searchContainer']/a")

        await q.fill("再见")
        await yoopu3_icon.click()


        # input()

        await browser.close()




if __name__ == "__main__":

    asyncio.get_event_loop().run_until_complete(example())



