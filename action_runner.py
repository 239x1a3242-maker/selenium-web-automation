def run_actions(engine, task):
    """
    Execute a sequence of automation actions with comprehensive error handling.
    
    Args:
        engine: Browser automation engine with required methods
        task: List of action dictionaries
    """
    for step_idx, step in enumerate(task, 1):
        try:
            action = step.get("action")
            if not action:
                print(f"\n[Step {step_idx}] Missing 'action' key: {step}")
                continue
                
            handlers = {
                "open": handle_open,
                "click": handle_click,
                "type": handle_type,
                "wait": handle_wait,
		"wait_seconds": handle_wait_seconds,
                "wait_for": handle_wait_for,
                "scroll_to": handle_scroll_to,
                "hover": handle_hover,
                "double_click": handle_double_click,
                "right_click": handle_right_click,
                "drag_drop": handle_drag_drop,
                "select_option": handle_select_option,
                "clear": handle_clear,
                "screenshot": handle_screenshot,
                "switch_window": handle_switch_window,
                "back": handle_back,
                "forward": handle_forward,
                "refresh": handle_refresh,
                "close": handle_close,
                "get_text": handle_get_text,
                "get_attribute": handle_get_attribute,
                "assert_visible": handle_assert_visible,
                "assert_text": handle_assert_text
            }
            
            if action in handlers:
                handlers[action](engine, step, step_idx)
            else:
                print(f"\n[Step {step_idx}] Unknown action '{action}': {step}")
                
        except Exception as e:
            print(f"\n❌ Automation failed at step {step_idx}:")
            print(f"   Action: {step}")
            print(f"   Error: {str(e)}")
            print(f"   Type: {type(e).__name__}")
            break
    
    print("\n✅ Automation sequence completed!")

# Action Handlers
def handle_open(engine, step, step_idx):
    """Navigate to URL"""
    url = step.get("url")
    if not url:
        raise ValueError("Missing 'url' parameter")
    print(f"[Step {step_idx}] 🌐 Opening: {url}")
    engine.open(url)

def handle_click(engine, step, step_idx):
    """Click element"""
    selector = step.get("selector")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    print(f"[Step {step_idx}] 🖱️ Clicking: {selector}")
    engine.click(selector)

def handle_type(engine, step, step_idx):
    """Type text into element"""
    selector = step.get("selector")
    value = step.get("value", "")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    print(f"[Step {step_idx}] ⌨️ Typing '{value[:20]}...' into: {selector}")
    engine.type(selector, value)

def handle_wait(engine, step, step_idx):
    """Wait for specified seconds"""
    seconds = step.get("seconds", 1)
    print(f"[Step {step_idx}] ⏳ Waiting {seconds}s...")
    engine.wait_seconds(seconds)

def handle_wait_seconds(engine, step, step_idx):
    """Wait for specified seconds"""
    seconds = step.get("seconds", 1)
    print(f"[Step {step_idx}] ⏳ Waiting {seconds}s...")
    engine.wait_seconds(seconds)

def handle_wait_for(engine, step, step_idx):
    """Wait for selector to appear"""
    selector = step.get("selector")
    timeout = step.get("timeout", 10)
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    print(f"[Step {step_idx}] ⌛ Waiting for: {selector} (timeout: {timeout}s)")
    engine.wait_for_selector(selector, timeout)

def handle_scroll_to(engine, step, step_idx):
    """Scroll to element or pixels"""
    selector = step.get("selector")
    pixels = step.get("pixels")
    
    if selector:
        print(f"[Step {step_idx}] 📜 Scrolling to: {selector}")
        engine.scroll_to_selector(selector)
    elif pixels:
        print(f"[Step {step_idx}] 📜 Scrolling {pixels}px")
        engine.scroll_pixels(pixels)
    else:
        raise ValueError("Provide either 'selector' or 'pixels'")

def handle_hover(engine, step, step_idx):
    """Hover over element"""
    selector = step.get("selector")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    print(f"[Step {step_idx}] 🖱️ Hovering: {selector}")
    engine.hover(selector)

def handle_double_click(engine, step, step_idx):
    """Double click element"""
    selector = step.get("selector")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    print(f"[Step {step_idx}] 🖱️ Double clicking: {selector}")
    engine.double_click(selector)

def handle_right_click(engine, step, step_idx):
    """Right click element"""
    selector = step.get("selector")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    print(f"[Step {step_idx}] 🖱️ Right clicking: {selector}")
    engine.right_click(selector)

def handle_drag_drop(engine, step, step_idx):
    """Drag from source to target"""
    source = step.get("source")
    target = step.get("target")
    if not source or not target:
        raise ValueError("Missing 'source' or 'target' parameter")
    print(f"[Step {step_idx}] 🖱️ Dragging {source} → {target}")
    engine.drag_drop(source, target)

def handle_select_option(engine, step, step_idx):
    """Select option from dropdown"""
    selector = step.get("selector")
    option = step.get("option")  # text, value, or index
    method = step.get("method", "text")  # text, value, index
    if not selector or not option:
        raise ValueError("Missing 'selector' or 'option' parameter")
    print(f"[Step {step_idx}] 📋 Selecting '{option}' from: {selector}")
    engine.select_option(selector, option, method)

def handle_clear(engine, step, step_idx):
    """Clear input field"""
    selector = step.get("selector")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    print(f"[Step {step_idx}] 🗑️ Clearing: {selector}")
    engine.clear(selector)

def handle_screenshot(engine, step, step_idx):
    """Take screenshot"""
    filename = step.get("filename", f"screenshot_step_{step_idx}.png")
    print(f"[Step {step_idx}] 📸 Screenshot: {filename}")
    engine.screenshot(filename)

def handle_switch_window(engine, step, step_idx):
    """Switch to window"""
    window = step.get("window")  # 'next', 'previous', or window_handle
    print(f"[Step {step_idx}] 🔄 Switching window: {window}")
    engine.switch_window(window)

def handle_back(engine, step, step_idx):
    """Go back in browser history"""
    print(f"[Step {step_idx}] ⬅️ Going back")
    engine.back()

def handle_forward(engine, step, step_idx):
    """Go forward in browser history"""
    print(f"[Step {step_idx}] ➡️ Going forward")
    engine.forward()

def handle_refresh(engine, step, step_idx):
    """Refresh current page"""
    print(f"[Step {step_idx}] 🔄 Refreshing page")
    engine.refresh()

def handle_close(engine, step, step_idx):
    """Close current window"""
    print(f"[Step {step_idx}] ❌ Closing window")
    engine.close()

def handle_get_text(engine, step, step_idx):
    """Get text from element (for verification)"""
    selector = step.get("selector")
    expected = step.get("expected")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    text = engine.get_text(selector)
    print(f"[Step {step_idx}] 📄 Text '{text[:50]}...' from: {selector}")
    if expected and text != expected:
        raise AssertionError(f"Expected '{expected}', got '{text}'")

def handle_get_attribute(engine, step, step_idx):
    """Get attribute value from element"""
    selector = step.get("selector")
    attr = step.get("attribute", "value")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    value = engine.get_attribute(selector, attr)
    print(f"[Step {step_idx}] 🔍 Attribute '{attr}': {value} from: {selector}")

def handle_assert_visible(engine, step, step_idx):
    """Assert element is visible"""
    selector = step.get("selector")
    if not selector:
        raise ValueError("Missing 'selector' parameter")
    visible = engine.is_visible(selector)
    print(f"[Step {step_idx}] ✅ '{selector}' {'visible' if visible else 'NOT visible'}")
    if not visible:
        raise AssertionError(f"Element not visible: {selector}")

def handle_assert_text(engine, step, step_idx):
    """Assert element contains expected text"""
    selector = step.get("selector")
    expected = step.get("expected")
    if not selector or not expected:
        raise ValueError("Missing 'selector' or 'expected' parameter")
    actual = engine.get_text(selector)
    print(f"[Step {step_idx}] ✅ Text check: '{actual}' == '{expected}'")
    if expected not in actual:
        raise AssertionError(f"Expected '{expected}', found '{actual}'")
