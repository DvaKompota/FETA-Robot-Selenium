*** Settings ***
Library           SeleniumLibrary  run_on_failure=Nothing


*** Variables ***
${home_url}                         http://automationpractice.com/

${header}                           //*[@id="header"]
${sign_in_button}                   //*[@class="login"]
${sign_out_button}                  //*[@class="logout"]
${account_button}                   //*[@class="account"]

${search_bar}                       //*[@id="search_query_top"]
${search_button}                    //button[@name="submit_search"]

${cart_block}                       //*[@class="shopping_cart"]
${cart_button}                      ${cart_block}/a
${cart_product_list}                ${cart_block}//*[@class="products"]
${cart_product_item}                ${cart_product_list}//*[contains(@data-id, "cart_block_product")]
${cart_checkout_button}             ${cart_block}//*[@id="button_order_cart"]

${top_menu}                         //*[@id="block_top_menu"]
${women_section}                    ${top_menu}//a[@title="Women"]
${dresses_section}                  ${top_menu}/ul/li/a[@title="Dresses"]
${tshirts_section}                  ${top_menu}/ul/li/a[@title="T-shirts"]

${homefeatured_list}                //*[@id="homefeatured"]
${product_container_xpath}          //*[@class="product-container"]
${product_img_link_xpath}           //*[@class="product_img_link"]
${product_name_xpath}               //*[@class="product-name"]
${product_price_xpath}              //*[@class="price"]
${add_to_cart_button_xpath}         //a[@title="Add to cart"]

${cart_overlay}                     //*[@id="layer_cart"]
${cart_overlay_checkout_button}     //*[@class="clearfix"]//*[@title="Proceed to checkout"]
${cart_overlay_close}               ${cart_overlay}//*[@title="Close window"]

${footer}                           //*[@id="footer"]
${facebook_button}                  ${footer}//*[@class="facebook"]
${twitter_button}                   ${footer}//*[@class="twitter"]
${youtube_button}                   ${footer}//*[@class="youtube"]
${google_button}                    ${footer}//*[@class="google-plus"]


*** Keywords ***
Open Home Page
    go to                           ${home_url}
    wait until element is visible   ${header}

List happy elements
    @{home_happy_elements}      create list    ${header}    ${sign_in_button}    ${search_bar}    ${cart_button}
    ...     ${top_menu}    ${women_section}    ${dresses_section}    ${tshirts_section}
    ...     ${footer}    ${facebook_button}    ${twitter_button}    ${youtube_button}    ${google_button}
    [Return]    @{home_happy_elements}

Validate happy elements
    @{happy_elements}    List happy elements
    FOR    ${element}   IN    @{happy_elements}
        element should be visible    ${element}
    END
