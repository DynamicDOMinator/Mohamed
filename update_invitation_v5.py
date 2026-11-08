# -*- coding: utf-8 -*-
"""
Generator for the Elegant Arabic Wedding Invitation Website - v5
Addressing user feedback:
1. 4-flap completely closed envelope (Top, Bottom, Left, Right).
   - When closed: 100% closed, zero white gaps or text peeking through.
   - When opened: opens in 4 directions (Top up, Bottom down, Left left, Right right).
2. For the first page, make the father's name:
   السيد/ وائل علي
   and make it stand out subtly in color.
3. Background texture: assets/floral-texture-bg.jpg with 20% opacity.
4. Single line countdown with no seconds, no boxes, no paragraph, no text under.
5. No footer at end of page.
6. No share/music buttons.
7. Details page: small frame, single line date/time, no paragraph, no footer photo credit.
8. Solid colors (no gradients).
"""

html_code = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#4a0e17">
  <title>دعوة عقد قران | محمد & روجين</title>

  <!-- Google Fonts: Aref Ruqaa for majestic names, Amiri for sacred texts, Alexandria for editorial body -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Alexandria:wght@300;400;500;600;700&family=Amiri:ital,wght@0,400;0,700;1,400&family=Aref+Ruqaa:wght@400;700&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================
       DESIGN SYSTEM: SOLID EDITORIAL LUXURY (NO GRADIENTS)
       ========================================================== */
    :root {
      --burgundy-deep: #38070e;
      --burgundy-main: #4a0e17;
      --burgundy-rich: #58141f;
      --burgundy-wine: #6e1d2a;
      --burgundy-light: #8e2b3c;
      --burgundy-tint: #f6eef0;

      --ivory-base: #faf7f2;
      --ivory-paper: #fdfcf9;
      --ivory-card: #f8f4ec;
      --champagne-tint: #f3ebdc;
      --champagne-gold: #c5a059;
      --champagne-bright: #d4af37;
      --gold-deep: #7d5e2a;
      --gold-honor: #8f6826; /* Distinguished gold for father's name */

      --text-main: #231417;
      --text-editorial: #453034;
      --text-muted: #6e575c;
      --text-light: #947e83;

      --border-subtle: #ebdcc4;
      --border-medium: #c5a059;
      --border-burgundy: #4a0e17;

      --shadow-soft: 0 8px 24px rgba(58, 10, 17, 0.05);
      --shadow-card: 0 14px 40px rgba(58, 10, 17, 0.08);
      --shadow-deep: 0 20px 55px rgba(58, 10, 17, 0.14);

      --font-names: 'Aref Ruqaa', 'Amiri', serif;
      --font-calligraphy: 'Amiri', serif;
      --font-body: 'Alexandria', 'Amiri', sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    html {
      scroll-behavior: smooth;
      background-color: var(--ivory-base);
      color: var(--text-main);
      width: 100%;
      max-width: 100vw;
      overflow-x: hidden !important;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--ivory-base);
      line-height: 1.9;
      font-size: 16px;
      width: 100%;
      max-width: 100vw;
      overflow-x: hidden !important;
      position: relative;
      margin: 0;
      padding: 0;
    }

    *, *::before, *::after {
      box-sizing: border-box;
    }

    /* ==========================================================
       USER-REQUESTED FLORAL TEXTURE BACKGROUND (20% OPACITY)
       ========================================================== */
    .floral-texture-bg-layer {
      position: fixed;
      inset: 0;
      background-image: url('assets/floral-texture-bg.jpg');
      background-repeat: repeat;
      background-size: 260px auto;
      opacity: 0.20; /* Exactly 20% Opacity */
      pointer-events: none;
      z-index: 0;
    }

    ::selection {
      background: var(--champagne-tint);
      color: var(--burgundy-deep);
    }

    a {
      text-decoration: none;
      color: inherit;
    }

    button {
      font-family: inherit;
      border: none;
      background: none;
      cursor: pointer;
    }

    /* Containers */
    .container {
      width: min(100% - 36px, 840px);
      margin-inline: auto;
      position: relative;
      z-index: 2;
    }

    .container-compact {
      width: min(100% - 36px, 580px);
      margin-inline: auto;
      position: relative;
      z-index: 2;
    }

    /* Solid Framing Lines */
    .luxury-frame-line {
      position: fixed;
      left: 0;
      right: 0;
      height: 3px;
      z-index: 999;
      pointer-events: none;
      background-color: var(--burgundy-main);
    }
    .frame-line-top { top: 0; border-bottom: 1px solid var(--champagne-gold); }
    .frame-line-bottom { bottom: 0; border-top: 1px solid var(--champagne-gold); }

    /* Delicate Falling Petals Canvas */
    #petalsCanvas {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 1;
    }

    /* Section Styling */
    .section {
      position: relative;
      padding: 80px 18px;
      text-align: center;
      z-index: 2;
    }

    .section-cream {
      background-color: rgba(248, 244, 236, 0.88);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }

    /* Section Crests & Dividers */
    .section-crest {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin-bottom: 14px;
      color: var(--champagne-gold);
    }

    .crest-line {
      width: 40px;
      height: 1px;
      background-color: var(--champagne-gold);
    }

    .crest-symbol {
      font-size: 15px;
      color: var(--champagne-gold);
      letter-spacing: 2px;
    }

    .section-title {
      font-family: var(--font-names);
      font-size: clamp(28px, 5.5vw, 38px);
      font-weight: 400;
      color: var(--burgundy-deep);
      margin-bottom: 8px;
      letter-spacing: -0.5px;
    }

    .section-subtitle {
      font-size: 15px;
      color: var(--text-muted);
      max-width: 500px;
      margin: 0 auto 30px;
      line-height: 1.8;
      font-weight: 400;
    }

    .divider-flourish {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin: 22px auto;
      max-width: 220px;
      color: var(--champagne-gold);
      opacity: 0.9;
    }

    .divider-flourish::before,
    .divider-flourish::after {
      content: "";
      flex: 1;
      height: 1px;
      background-color: var(--champagne-gold);
      opacity: 0.5;
    }

    /* ==========================================================
       PAGE 1: AUTHENTIC EMBOSSED BURGUNDY ENVELOPE (CLOSED LOOK)
       - Rounded tongue flap overlapping center like reference photo
       - Central wax seal stamp on top of the tongue
       - Opens with zero phone overflow (inward 3D foreshorten)
       ========================================================== */
    .envelope-hero-section {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 40px 16px 50px;
      position: relative;
      text-align: center;
      z-index: 2;
      width: 100%;
      max-width: 100vw;
      overflow-x: clip !important;
      overflow-y: visible;
    }

    .envelope-stage-box {
      max-width: min(580px, calc(100vw - 28px));
      width: 100%;
      margin: 0 auto;
      perspective: 1400px;
      position: relative;
    }

    /* Outer Burgundy Folio Envelope Container */
    .burgundy-folio-envelope {
      width: 100%;
      position: relative;
      border-radius: 6px;
      box-shadow: 0 16px 50px rgba(45, 6, 12, 0.35);
      background-color: var(--burgundy-rich);
      background-image: url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: center;
      border: 1.5px solid var(--champagne-gold);
      min-height: 520px;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: visible;
    }

    /* 4-FLAP CONTAINER: 100% COVERAGE & MATCHING REFERENCE PHOTO */
    .envelope-4flaps-container {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 20;
      overflow: visible;
    }

    /* Common styling for all 4 flaps:
       They all share inset: 0 and the exact same background image & alignment,
       guaranteeing seamless floral texture continuity across the entire envelope! */
    .flap-envelope-common {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      background-color: var(--burgundy-rich);
      background-image: url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: center;
      transform-style: preserve-3d;
      transition: transform 0.75s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.6s ease;
      pointer-events: none;
    }

    /* 1. LEFT FLAP (Underneath the tongue) */
    .flap-panel-left {
      clip-path: url(#clipFlapLeft);
      -webkit-clip-path: url(#clipFlapLeft);
      transform-origin: left center;
      z-index: 22;
    }

    /* 2. TOP FLAP */
    .flap-panel-top {
      clip-path: url(#clipFlapTop);
      -webkit-clip-path: url(#clipFlapTop);
      transform-origin: top center;
      z-index: 23;
      filter: drop-shadow(0 3px 6px rgba(25, 3, 6, 0.4));
    }

    /* 3. BOTTOM FLAP */
    .flap-panel-bottom {
      clip-path: url(#clipFlapBottom);
      -webkit-clip-path: url(#clipFlapBottom);
      transform-origin: bottom center;
      z-index: 24;
      filter: drop-shadow(0 -3px 6px rgba(25, 3, 6, 0.4));
    }

    /* 4. RIGHT FLAP: AUTHENTIC ROUNDED TONGUE OVERLAPPING THE CENTER (ON TOP) */
    .flap-panel-right {
      clip-path: url(#clipFlapRightTongue);
      -webkit-clip-path: url(#clipFlapRightTongue);
      transform-origin: right center;
      z-index: 25;
      filter: drop-shadow(-3px 1px 7px rgba(25, 3, 6, 0.5));
    }

    /* CENTRAL WAX SEAL */
    .wax-seal-center-action {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 35;
      cursor: pointer;
      transition: all 0.4s ease;
    }

    .wax-seal-center-action:hover {
      transform: translate(-50%, -50%) scale(1.07);
    }

    .wax-seal-button-disc {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background-color: var(--burgundy-main);
      box-shadow: 
        0 10px 25px rgba(35, 4, 8, 0.6),
        inset 0 2px 4px rgba(255, 255, 255, 0.25);
      border: 2px solid var(--champagne-gold);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      position: relative;
    }

    .wax-seal-button-disc::before {
      content: "";
      position: absolute;
      inset: 4px;
      border-radius: 50%;
      border: 1px dashed rgba(197, 160, 89, 0.5);
      pointer-events: none;
    }

    .seal-monogram-text {
      font-family: var(--font-names);
      font-size: 28px;
      font-weight: 700;
      line-height: 1;
    }

    .seal-ribbon-tails {
      position: absolute;
      bottom: -20px;
      left: 50%;
      transform: translateX(-50%);
      width: 48px;
      height: 26px;
      display: flex;
      justify-content: center;
      gap: 5px;
      z-index: -1;
    }

    .ribbon-blade {
      width: 15px;
      height: 28px;
      background-color: var(--champagne-gold);
      clip-path: polygon(0 0, 100% 0, 100% 80%, 50% 100%, 0 80%);
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
    }
    .ribbon-blade.left { transform: rotate(15deg); }
    .ribbon-blade.right { transform: rotate(-15deg); }

    /* Open Prompt Pill */
    .unfold-pill-prompt {
      position: absolute;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      background-color: #ffffff;
      border: 1px solid var(--champagne-gold);
      color: var(--burgundy-deep);
      padding: 9px 22px;
      border-radius: 30px;
      font-size: 14.5px;
      font-weight: 600;
      white-space: nowrap;
      box-shadow: 0 8px 24px rgba(45, 6, 12, 0.25);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      transition: all 0.3s ease;
      z-index: 35;
    }

    .unfold-pill-prompt:hover {
      background-color: var(--ivory-paper);
      border-color: var(--burgundy-main);
      color: var(--burgundy-main);
    }

    /* ----------------------------------------------------
       THE INNER UNFOLDED INVITATION CARD
       Completely hidden while closed!
       Opens when the 4 flaps open.
       ---------------------------------------------------- */
    .inner-unfolded-card {
      width: 100%;
      background-color: rgba(255, 255, 255, 0.97);
      padding: 48px 30px 42px;
      border-radius: 4px;
      text-align: center;
      position: relative;
      z-index: 10;
      border: 1px solid var(--border-medium);
      box-shadow: 
        inset 0 0 0 6px #ffffff,
        inset 0 0 0 7.5px var(--border-subtle);
      transition: all 0.85s cubic-bezier(0.16, 1, 0.3, 1);
      opacity: 0;
      pointer-events: none;
      transform: scale(0.96);
    }

    /* Subtle Botanical Corner Filigrees on Inner Card */
    .corner-floral-filigree {
      position: absolute;
      width: 32px;
      height: 32px;
      color: var(--champagne-gold);
      pointer-events: none;
      opacity: 0.8;
    }
    .filigree-tr { top: 10px; right: 10px; }
    .filigree-tl { top: 10px; left: 10px; transform: scaleX(-1); }
    .filigree-br { bottom: 10px; right: 10px; transform: scaleY(-1); }
    .filigree-bl { bottom: 10px; left: 10px; transform: scale(-1); }

    .inner-card-flora-header {
      width: 130px;
      height: 28px;
      margin: 0 auto 12px;
      color: var(--champagne-gold);
    }

    .bismillah-text {
      font-family: var(--font-calligraphy);
      font-size: clamp(21px, 4.4vw, 27px);
      color: var(--burgundy-rich);
      margin: 0 0 14px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }

    .invitation-honor-phrase {
      font-size: clamp(16px, 3.2vw, 18.5px);
      color: var(--text-editorial);
      line-height: 1.8;
      margin-bottom: 16px;
      font-weight: 500;
    }

    /* STACKED NAMES BLOCK */
    .stacked-names-flow {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      margin: 8px auto 20px;
      padding: 14px 20px;
      background-color: var(--ivory-card);
      border-top: 1px solid var(--border-medium);
      border-bottom: 1px solid var(--border-medium);
      border-radius: 4px;
      max-width: 480px;
    }

    .stacked-name-groom {
      font-family: var(--font-names);
      font-size: clamp(44px, 8.5vw, 68px);
      color: var(--burgundy-main);
      line-height: 1.2;
      font-weight: 700;
      letter-spacing: -0.5px;
    }

    .stacked-bridge-phrase {
      font-size: clamp(16px, 3.2vw, 19px);
      color: var(--text-editorial);
      font-weight: 500;
      margin: 3px 0;
    }

    /* USER-REQUESTED FATHER'S NAME STYLING:
       "for the first page make the name السيد/ وائل علي and make it stand out subtly in color" */
    .vip-father-name {
      color: var(--gold-honor); /* Distinguished antique champagne gold */
      font-weight: 700;
      font-size: 1.08em;
      letter-spacing: 0.3px;
      display: inline-block;
      padding: 0 5px;
      border-bottom: 1.5px solid var(--champagne-gold);
    }

    .stacked-name-bride {
      font-family: var(--font-names);
      font-size: clamp(44px, 8.5vw, 68px);
      color: var(--burgundy-main);
      line-height: 1.2;
      font-weight: 700;
      letter-spacing: -0.5px;
    }

    .heartfelt-body-text {
      font-size: clamp(15px, 3vw, 17.5px);
      color: var(--text-muted);
      line-height: 2;
      max-width: 500px;
      margin: 14px auto 18px;
      font-weight: 400;
    }

    .prophetic-dua-badge {
      display: inline-block;
      padding: 10px 22px;
      background-color: var(--ivory-card);
      border: 1px solid var(--champagne-gold);
      border-radius: 40px;
      box-shadow: var(--shadow-soft);
      margin: 6px 0 24px;
    }

    .prophetic-dua-content {
      font-family: var(--font-calligraphy);
      font-size: clamp(16px, 3.2vw, 19.5px);
      color: var(--burgundy-rich);
      font-weight: 700;
      letter-spacing: 0.3px;
    }

    /* Small "عرض التفاصيل" Button */
    .inner-card-button-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      margin-top: 10px;
    }

    .btn-details-compact {
      background-color: var(--burgundy-main);
      color: #ffffff;
      padding: 8px 18px;
      border-radius: 4px;
      font-size: 13.5px;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border: 1px solid var(--burgundy-main);
      box-shadow: 0 4px 12px rgba(74, 14, 23, 0.18);
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .btn-details-compact:hover {
      background-color: var(--burgundy-rich);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(74, 14, 23, 0.28);
    }

    .btn-fold-compact {
      background-color: transparent;
      color: var(--burgundy-main);
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 13.5px;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border: 1px solid var(--border-medium);
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .btn-fold-compact:hover {
      background-color: var(--ivory-card);
      border-color: var(--burgundy-main);
      transform: translateY(-2px);
    }

    /* ==========================================================
       OPENED STATE: FLAPS UNFOLD IN-BOUNDS (ZERO PHONE OVERFLOW)
       - Swings forward towards viewer (max 85deg) while fading out
       - NEVER extends beyond envelope boundaries horizontally or vertically
       - Wax seal lifts away
       - Inner card scales in smoothly with elevated luxury depth
       ========================================================== */
    .envelope-stage-box.is-opened .flap-panel-right {
      transform: rotateY(85deg) scale(0.96);
      opacity: 0;
      pointer-events: none;
    }

    .envelope-stage-box.is-opened .flap-panel-left {
      transform: rotateY(-85deg) scale(0.96);
      opacity: 0;
      pointer-events: none;
    }

    .envelope-stage-box.is-opened .flap-panel-top {
      transform: rotateX(85deg) translateY(-10px);
      opacity: 0;
      pointer-events: none;
    }

    .envelope-stage-box.is-opened .flap-panel-bottom {
      transform: rotateX(-85deg) translateY(10px);
      opacity: 0;
      pointer-events: none;
    }

    .envelope-stage-box.is-opened .wax-seal-center-action {
      transform: translate(-50%, -180px) scale(0.65);
      opacity: 0;
      pointer-events: none;
    }

    .envelope-stage-box.is-opened .unfold-pill-prompt {
      opacity: 0;
      pointer-events: none;
      visibility: hidden;
    }

    .envelope-stage-box.is-opened .inner-unfolded-card {
      opacity: 1;
      pointer-events: auto;
      transform: scale(1);
      z-index: 30; /* rises prominently above opened flaps */
    }

    /* ==========================================================
       SECTION 2: WEDDING DETAILS & VENUE
       Smaller frame, smaller text, timing in single line (no frames),
       paragraph removed, footer text removed, no couple names here.
       ========================================================== */
    .venue-compact-card {
      max-width: 580px;
      margin: 0 auto;
      background-color: rgba(253, 252, 249, 0.95);
      border-radius: 6px;
      border: 1px solid var(--border-medium);
      box-shadow: var(--shadow-card);
      overflow: hidden;
      position: relative;
    }

    .venue-photo-compact-frame {
      position: relative;
      width: 100%;
      height: 220px;
      overflow: hidden;
      background-color: #2b1216;
    }

    .venue-photo-actual {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 38%;
      display: block;
      transition: transform 0.6s ease;
    }

    .venue-compact-card:hover .venue-photo-actual {
      transform: scale(1.03);
    }

    .venue-photo-badge {
      position: absolute;
      bottom: 14px;
      right: 18px;
      background-color: var(--ivory-paper);
      padding: 5px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      color: var(--burgundy-deep);
      border: 1px solid var(--border-subtle);
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.15);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .mosque-metadata-compact-strip {
      background-color: var(--ivory-card);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 18px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      text-align: right;
    }

    .mosque-metadata-text {
      font-size: 12.5px;
      color: var(--text-editorial);
      line-height: 1.5;
    }

    .mosque-rating-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: #ffffff;
      padding: 4px 10px;
      border-radius: 16px;
      border: 1px solid var(--border-subtle);
      font-size: 12px;
    }

    .rating-stars-solid {
      color: #e5b338;
      font-size: 13px;
      letter-spacing: 1px;
    }

    .rating-label {
      font-weight: 600;
      color: var(--burgundy-main);
    }

    .venue-compact-body {
      padding: 24px 20px 28px;
      text-align: center;
    }

    .venue-compact-title {
      font-family: var(--font-names);
      font-size: clamp(26px, 5vw, 34px);
      color: var(--burgundy-deep);
      margin-bottom: 4px;
      font-weight: 400;
    }

    .venue-compact-address {
      color: var(--text-muted);
      font-size: 14.5px;
      line-height: 1.6;
      margin-bottom: 18px;
    }

    /* FULL TIME & DATE IN A SINGLE LINE (NO FRAMES) */
    .timing-single-line-container {
      background-color: var(--ivory-card);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      padding: 13px 18px;
      margin: 16px auto 22px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      color: var(--burgundy-deep);
      font-weight: 700;
      font-size: clamp(14.5px, 3.2vw, 16.5px);
    }

    .timing-icon-badge {
      color: var(--champagne-gold);
      font-size: 18px;
    }

    /* Google Maps Button */
    .btn-maps-solid {
      background-color: var(--burgundy-main);
      color: #ffffff;
      padding: 11px 26px;
      border-radius: 4px;
      font-size: 14.5px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 15px rgba(74, 14, 23, 0.2);
      border: 1px solid var(--burgundy-main);
      transition: all 0.3s ease;
    }

    .btn-maps-solid:hover {
      background-color: var(--burgundy-rich);
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(74, 14, 23, 0.3);
      color: #ffffff;
    }

    .btn-maps-solid svg {
      width: 18px;
      height: 18px;
      color: var(--champagne-bright);
    }

    /* ==========================================================
       SECTION 3: COUNTDOWN IN SINGLE LINE
       - Paragraph removed
       - Boxes removed
       - Single line with NO seconds
       - Text under removed
       ========================================================== */
    .countdown-single-line-wrapper {
      max-width: 580px;
      margin: 20px auto 0;
      background-color: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      padding: 18px 22px;
      box-shadow: var(--shadow-soft);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }

    .countdown-timer-text {
      font-family: var(--font-names);
      font-size: clamp(24px, 5.2vw, 36px);
      font-weight: 700;
      color: var(--burgundy-main);
      line-height: 1.2;
      direction: rtl;
    }

    /* ==========================================================
       SECTION 4: IMPORTANT NOTES
       ========================================================== */
    .notes-compact-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      max-width: 680px;
      margin: 0 auto;
    }

    .note-card-box {
      background-color: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      padding: 28px 22px;
      text-align: right;
      position: relative;
      box-shadow: var(--shadow-soft);
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .note-card-box:hover {
      transform: translateY(-2px);
      border-color: var(--burgundy-main);
      box-shadow: var(--shadow-card);
    }

    .note-top-header {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .note-icon-pod {
      width: 48px;
      height: 48px;
      border-radius: 10px;
      background-color: var(--ivory-card);
      border: 1px solid var(--border-medium);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .note-icon-pod svg {
      width: 32px;
      height: 32px;
    }

    .note-heading-title {
      font-family: var(--font-names);
      font-size: 21px;
      color: var(--burgundy-deep);
      font-weight: 400;
    }

    .note-paragraph {
      color: var(--text-editorial);
      font-size: 14.5px;
      line-height: 2;
      font-weight: 400;
    }

    /* ==========================================================
       SECTION 5: CLOSING SECTION (NO FOOTER AT END)
       ========================================================== */
    .closing-section-wrapper {
      padding: 90px 18px 95px;
      background-color: transparent;
      text-align: center;
      position: relative;
      z-index: 2;
    }

    .closing-content-card {
      max-width: 600px;
      margin: 0 auto;
      padding: 48px 30px;
      background-color: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      box-shadow: var(--shadow-card);
      position: relative;
    }

    .closing-warm-headline {
      font-family: var(--font-names);
      font-size: clamp(32px, 6.5vw, 46px);
      color: var(--burgundy-deep);
      font-weight: 400;
      margin-bottom: 16px;
    }

    .closing-farewell-text {
      font-size: clamp(15.5px, 3vw, 18px);
      color: var(--text-editorial);
      line-height: 2.1;
      max-width: 500px;
      margin: 0 auto 24px;
    }

    .closing-floral-emblem {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin: 16px auto 0;
      color: var(--champagne-gold);
      font-size: 19px;
    }

    /* Responsiveness */
    @media (max-width: 768px) {
      html, body {
        width: 100%;
        max-width: 100vw;
        overflow-x: hidden !important;
      }

      .envelope-hero-section {
        padding: 30px 10px 40px;
        width: 100%;
        max-width: 100vw;
        overflow-x: clip !important;
      }

      .envelope-stage-box {
        max-width: calc(100vw - 20px);
        width: 100%;
      }

      .burgundy-folio-envelope {
        min-height: 480px;
      }

      .section {
        padding: 50px 12px;
      }

      .inner-unfolded-card {
        padding: 32px 14px 26px;
      }

      .stacked-names-flow {
        padding: 10px 10px;
        margin: 8px 0 14px;
      }

      .stacked-name-groom, .stacked-name-bride {
        font-size: clamp(34px, 8.5vw, 52px);
      }

      .bismillah-text {
        font-size: 20px;
      }

      .invitation-honor-phrase {
        font-size: 14.5px;
      }

      .notes-compact-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }

      .venue-photo-compact-frame {
        height: 180px;
      }

      .mosque-metadata-compact-strip {
        flex-direction: column;
        align-items: flex-start;
      }

      .countdown-single-line-wrapper {
        padding: 12px 14px;
      }

      .countdown-timer-text {
        font-size: 22px;
      }
    }
  </style>
</head>
<body>

  <!-- Background Texture Layer with 20% Opacity as requested -->
  <div class="floral-texture-bg-layer" aria-hidden="true"></div>

  <!-- Hidden SVG Definitions for Envelope Flap Clips & Filigrees -->
  <svg style="position:absolute; width:0; height:0; overflow:hidden; pointer-events:none;" aria-hidden="true">
    <defs>
      <!-- Right flap with authentic rounded tongue matching user reference image -->
      <clipPath id="clipFlapRightTongue" clipPathUnits="objectBoundingBox">
        <path d="M 1 0 L 0.50 0.42 C 0.41 0.44, 0.41 0.56, 0.50 0.58 L 1 1 Z" />
      </clipPath>
      <!-- Left flap meeting under the tongue -->
      <clipPath id="clipFlapLeft" clipPathUnits="objectBoundingBox">
        <path d="M 0 0 L 0.51 0.50 L 0 1 Z" />
      </clipPath>
      <!-- Top flap -->
      <clipPath id="clipFlapTop" clipPathUnits="objectBoundingBox">
        <path d="M 0 0 L 1 0 L 0.50 0.51 Z" />
      </clipPath>
      <!-- Bottom flap -->
      <clipPath id="clipFlapBottom" clipPathUnits="objectBoundingBox">
        <path d="M 0 1 L 1 1 L 0.50 0.49 Z" />
      </clipPath>
    </defs>
    <symbol id="corner-filigree-flora" viewBox="0 0 40 40">
      <path fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"
        d="M2,38 L2,10 C2,5.6 5.6,2 10,2 L38,2 M6,34 L6,12 C6,8.7 8.7,6 12,6 L34,6 M10,10 L18,18" />
    </symbol>

    <symbol id="floral-center-ornament" viewBox="0 0 200 40">
      <path fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"
        d="M10,20 Q60,6 90,20 Q95,6 100,6 Q105,6 110,20 Q140,6 190,20 M100,6 L100,34 M85,20 C85,15 95,15 100,20 C105,15 115,15 115,20" />
      <circle cx="100" cy="6" r="2.5" fill="currentColor" />
      <circle cx="70" cy="18" r="1.5" fill="currentColor" />
      <circle cx="130" cy="18" r="1.5" fill="currentColor" />
    </symbol>
  </svg>

  <!-- Luxury Framing Lines (Solid) -->
  <div class="luxury-frame-line frame-line-top" aria-hidden="true"></div>
  <div class="luxury-frame-line frame-line-bottom" aria-hidden="true"></div>

  <!-- Delicate Falling Petals Canvas -->
  <canvas id="petalsCanvas" aria-hidden="true"></canvas>

  <!-- ==========================================================
       PAGE 1: COMPLETELY CLOSED 4-FLAP ENVELOPE (ZERO GAPS)
       Opens with 4 flaps (Top, Bottom, Left, Right)
       Contains:
       - بسم الله الرحمن الرحيم
       - نتشرف بدعوتكم لحضور حفل عقد قران
       - محمد
       - على كريمة السيد/ وائل علي (standing out subtly in color)
       - روجين
       - بقلوب يملؤها الفرح...
       - بارك الله لهما...
       - Compact details button
       ========================================================== -->
  <header class="envelope-hero-section" id="invitation-hero">
    <div class="envelope-stage-box" id="envelopeStage">

      <div class="burgundy-folio-envelope">

        <!-- 4 OVERLAPPING FLAPS (AUTHENTIC REFERENCE LOOK & ROUNDED TONGUE) -->
        <div class="envelope-4flaps-container" aria-hidden="true">
          <div class="flap-envelope-common flap-panel-left" id="flapLeft"></div>
          <div class="flap-envelope-common flap-panel-top" id="flapTop"></div>
          <div class="flap-envelope-common flap-panel-bottom" id="flapBottom"></div>
          <div class="flap-envelope-common flap-panel-right" id="flapRight"></div>
        </div>

        <!-- Central Wax Seal with Monogram -->
        <div class="wax-seal-center-action" id="waxSealButton" onclick="toggleHeroEnvelope()" role="button" tabindex="0" aria-label="اضغط لفتح بطاقة الدعوة">
          <div class="wax-seal-button-disc">
            <span class="seal-monogram-text">م & ر</span>
          </div>
          <div class="seal-ribbon-tails">
            <div class="ribbon-blade left"></div>
            <div class="ribbon-blade right"></div>
          </div>
        </div>

        <!-- Open Prompt Pill -->
        <button type="button" class="unfold-pill-prompt" id="btnPromptUnfold" onclick="toggleHeroEnvelope()">
          <span>انقر لفتح بطاقة الدعوة</span>
          <span style="color:var(--champagne-gold); font-size:15px;">✦</span>
        </button>

        <!-- Inner Letterpress Invitation Card (Completely concealed while closed) -->
        <article class="inner-unfolded-card" id="innerInvitationCard">

          <!-- Corner Floral Filigrees -->
          <svg class="corner-floral-filigree filigree-tr" aria-hidden="true"><use href="#corner-filigree-flora" /></svg>
          <svg class="corner-floral-filigree filigree-tl" aria-hidden="true"><use href="#corner-filigree-flora" /></svg>
          <svg class="corner-floral-filigree filigree-br" aria-hidden="true"><use href="#corner-filigree-flora" /></svg>
          <svg class="corner-floral-filigree filigree-bl" aria-hidden="true"><use href="#corner-filigree-flora" /></svg>

          <svg class="inner-card-flora-header" aria-hidden="true">
            <use href="#floral-center-ornament" />
          </svg>

          <!-- 1. Bismillah -->
          <p class="bismillah-text">
            بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
          </p>

          <!-- 2. Invitation Phrase -->
          <p class="invitation-honor-phrase">
            نتشرف بدعوتكم لحضور حفل عقد قران
          </p>

          <!-- 3. STACKED NAMES WITH "السيد/ وائل علي" STANDING OUT SUBTLY IN COLOR -->
          <div class="stacked-names-flow">
            <h1 class="stacked-name-groom">محمد</h1>
            <p class="stacked-bridge-phrase">
              على كريمة <span class="vip-father-name">السيد/ وائل علي</span>
            </p>
            <h2 class="stacked-name-bride">روجين</h2>
          </div>

          <!-- 4. Heartfelt Greeting -->
          <p class="heartfelt-body-text">
            بقلوب يملؤها الفرح والسرور، يسعدنا دعوتكم لتشاركونا أجمل لحظات العمر، بحضوركم تكتمل فرحتنا.
          </p>

          <!-- 5. Prophetic Dua -->
          <div class="prophetic-dua-badge">
            <span class="prophetic-dua-content">
              بارك الله لهما وبارك عليهما وجمع بينهما في خير
            </span>
          </div>

          <!-- Buttons: Small "عرض التفاصيل" & Fold -->
          <div class="inner-card-button-row">
            <a href="#wedding-details" class="btn-details-compact" onclick="smoothScrollTo(event, '#wedding-details')">
              <span>عرض التفاصيل</span>
              <span>↓</span>
            </a>
            <button type="button" class="btn-fold-compact" onclick="toggleHeroEnvelope()">
              <span id="labelToggleEnvelope">طي البطاقة</span>
              <span>▲</span>
            </button>
          </div>

        </article>

      </div>

    </div>
  </header>

  <!-- ==========================================================
       SECTION 2: WEDDING DETAILS & VENUE
       - Text and frame smaller
       - Timing as full time in single line (not in frames)
       - Paragraph removed
       - Footer photo attribution removed
       - No couple names here
       ========================================================== -->
  <section class="section section-cream" id="wedding-details">
    <div class="container-compact">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">❖</span>
        <div class="crest-line"></div>
      </div>

      <h2 class="section-title">تفاصيل الحفل والمكان</h2>

      <article class="venue-compact-card">

        <!-- Compact Mosque Photo -->
        <div class="venue-photo-compact-frame">
          <img 
            id="venueMosquePhoto"
            class="venue-photo-actual"
            src="assets/al-hosary-mosque.jpg"
            alt="مسجد الحصري - ميدان الحصري، 6 أكتوبر"
            loading="lazy"
            decoding="async"
            onerror="this.onerror=null; this.src='https://upload.wikimedia.org/wikipedia/commons/4/45/Al-Hosary_Mosque_01.jpg';"
          >
          <div class="venue-photo-badge">
            <span>مسجد الحصري</span>
            <span style="color:var(--champagne-gold)">✦</span>
            <span>6 أكتوبر</span>
          </div>
        </div>

        <!-- Official Mosque Strip with 5 Stars -->
        <div class="mosque-metadata-compact-strip">
          <div class="mosque-metadata-text">
            <strong>Al-Hosary Mosque</strong> · ميدان الحصري، First 6th of October, Giza Governorate 12563, Egypt
          </div>
          <div class="mosque-rating-pill" title="تقييم 5 نجوم على خرائط Google">
            <span class="rating-stars-solid">★★★★★</span>
            <span class="rating-label">· Mosque</span>
          </div>
        </div>

        <div class="venue-compact-body">

          <h3 class="venue-compact-title">مسجد الحصري</h3>
          <p class="venue-compact-address">ميدان الحصري، 6 أكتوبر، الجيزة</p>

          <!-- FULL TIME & DATE IN A SINGLE LINE (NOT IN FRAMES) -->
          <div class="timing-single-line-container">
            <span class="timing-icon-badge">🗓</span>
            <span>الجمعة، 13 نوفمبر 2026 — الساعة 3:30 مساءً</span>
          </div>

          <!-- Google Maps Button -->
          <a 
            class="btn-maps-solid"
            id="btnGoogleDirections"
            href="https://maps.app.goo.gl/gx99A4hY75tbNW6e8"
            target="_blank"
            rel="noopener noreferrer"
            title="الاتجاهات عبر خرائط Google"
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
              <circle cx="12" cy="10" r="3"></circle>
            </svg>
            <span>الاتجاهات عبر خرائط Google</span>
          </a>

        </div>

      </article>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 3: COUNTDOWN IN SINGLE LINE
       - Paragraph removed
       - Boxes removed
       - Single line with NO seconds
       - Text under removed
       ========================================================== -->
  <section class="section" id="wedding-countdown">
    <div class="container-compact">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">⌛</span>
        <div class="crest-line"></div>
      </div>

      <h2 class="section-title">الوقت المتبقي حتى نلتقي</h2>

      <!-- SINGLE LINE COUNTDOWN (NO BOXES, NO SECONDS, NO TEXT UNDER) -->
      <div class="countdown-single-line-wrapper">
        <span style="color:var(--champagne-gold); font-size:20px;" aria-hidden="true">⏳</span>
        <div class="countdown-timer-text" id="countdownSingleLine" aria-live="polite">--</div>
      </div>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 4: IMPORTANT NOTES
       ========================================================== -->
  <section class="section section-cream" id="important-guest-notes">
    <div class="container">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">✦</span>
        <div class="crest-line"></div>
      </div>

      <h2 class="section-title">ملاحظات تهم ضيوفنا</h2>
      <p class="section-subtitle">
        حرصًا منا على راحتكم وتيسير حضوركم في هذا اليوم الاستثنائي
      </p>

      <div class="notes-compact-grid">

        <!-- Parking Note -->
        <article class="note-card-box">
          <div class="note-top-header">
            <div class="note-icon-pod" aria-hidden="true">
              <!-- Solid 3D Styled Car in Website Colors -->
              <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <ellipse cx="32" cy="50" rx="20" ry="4" fill="#38070e" opacity="0.15"/>
                <path d="M8 38L14 27C16 23 20 21 25 21H39C44 21 48 23 50 27L56 38C58 40 58 44 56 46H8C6 44 6 40 8 38Z" fill="#4a0e17" stroke="#c5a059" stroke-width="1.2"/>
                <path d="M16 28L20 23H44L48 28H16Z" fill="#ffffff" opacity="0.85"/>
                <circle cx="13" cy="38" r="2.5" fill="#d4af37"/>
                <circle cx="51" cy="38" r="2.5" fill="#d4af37"/>
                <circle cx="18" cy="46" r="6" fill="#231417"/>
                <circle cx="18" cy="46" r="3" fill="#c5a059"/>
                <circle cx="46" cy="46" r="6" fill="#231417"/>
                <circle cx="46" cy="46" r="3" fill="#c5a059"/>
              </svg>
            </div>
            <h3 class="note-heading-title">موقف السيارات</h3>
          </div>
          <p class="note-paragraph">
            نظرًا لاحتمالية وجود ازدحام مروري وصعوبة العثور على أماكن لركن السيارات، نرجو من حضراتكم مراعاة ذلك عند تحديد موعد الوصول.
          </p>
        </article>

        <!-- Separate Halls Note -->
        <article class="note-card-box">
          <div class="note-top-header">
            <div class="note-icon-pod" aria-hidden="true">
              <!-- Solid 3D Styled Dual Arches in Website Colors -->
              <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <ellipse cx="32" cy="52" rx="20" ry="3.5" fill="#38070e" opacity="0.12"/>
                <path d="M12 48V28C12 21.37 16.48 16 22 16C27.52 16 32 21.37 32 28V48H12Z" fill="#ffffff" stroke="#c5a059" stroke-width="1.2"/>
                <path d="M16 48V29C16 24 18.69 20 22 20C25.31 20 28 24 28 29V48H16Z" fill="#4a0e17"/>
                <path d="M32 48V28C32 21.37 36.48 16 42 16C47.52 16 52 21.37 52 28V48H32Z" fill="#ffffff" stroke="#c5a059" stroke-width="1.2"/>
                <path d="M36 48V29C36 24 38.69 20 42 20C45.31 20 48 24 48 29V48H36Z" fill="#4a0e17"/>
                <circle cx="32" cy="14" r="2.5" fill="#c5a059"/>
              </svg>
            </div>
            <h3 class="note-heading-title">تنظيم القاعات</h3>
          </div>
          <p class="note-paragraph">
            نود التنويه إلى أن قاعات الرجال والسيدات منفصلة، وذلك لضمان راحة جميع ضيوفنا.
          </p>
        </article>

      </div>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 5: CLOSING SECTION (NO FOOTER AT END)
       ========================================================== -->
  <section class="closing-section-wrapper" id="closing-farewell">
    <div class="container">
      <div class="closing-content-card">

        <svg style="width:140px; height:28px; margin:0 auto 16px; color:var(--champagne-gold);" aria-hidden="true">
          <use href="#floral-center-ornament" />
        </svg>

        <h2 class="closing-warm-headline">
          بوجودكم تكتمل فرحتنا
        </h2>

        <p class="closing-farewell-text">
          نسعد بحضوركم ومشاركتكم أجمل أيامنا، ونتمنى أن يجمعنا بكم دائمًا الخير والفرح.
        </p>

        <div class="divider-flourish" aria-hidden="true">
          <span>❦</span>
        </div>

        <div class="closing-floral-emblem" aria-hidden="true">
          <span>✤</span>
          <span>دمتم في خير ومحبة</span>
          <span>✤</span>
        </div>

      </div>
    </div>
  </section>

  <!-- ==========================================================
       JAVASCRIPT
       ========================================================== -->
  <script>
    /* ----------------------------------------------------
       1. WEDDING DATE & TARGET TIMESTAMP
       Friday, 13 November 2026 - 3:30 PM Cairo Time (UTC+2)
       ---------------------------------------------------- */
    const WEDDING_TARGET_ISO = "2026-11-13T15:30:00+02:00";
    const targetTime = new Date(WEDDING_TARGET_ISO).getTime();

    const arabicNumberFormat = new Intl.NumberFormat("ar-EG", { useGrouping: false });

    function toArabicNumeral(num) {
      if (isNaN(num)) return "٠";
      return arabicNumberFormat.format(num);
    }

    /* ----------------------------------------------------
       2. COUNTDOWN IN SINGLE LINE (NO SECONDS)
       ---------------------------------------------------- */
    const elCountdownLine = document.getElementById("countdownSingleLine");

    function runCountdownTick() {
      const now = Date.now();
      const diff = targetTime - now;

      if (diff <= 0) {
        if (elCountdownLine) {
          elCountdownLine.textContent = "اليوم هو يوم فرحتنا المبارك، مرحبًا بكم جميعًا!";
        }
        return;
      }

      const totalMinutes = Math.floor(diff / (1000 * 60));
      const days = Math.floor(totalMinutes / (60 * 24));
      const hours = Math.floor((totalMinutes % (60 * 24)) / 60);
      const minutes = totalMinutes % 60;

      if (elCountdownLine) {
        elCountdownLine.textContent = toArabicNumeral(days) + " يوم  •  " + toArabicNumeral(hours) + " ساعة  •  " + toArabicNumeral(minutes) + " دقيقة";
      }
    }

    runCountdownTick();
    setInterval(runCountdownTick, 1000);

    /* ----------------------------------------------------
       3. INTERACTIVE 4-FLAP ENVELOPE UNFOLDING
       ---------------------------------------------------- */
    const envelopeStage = document.getElementById("envelopeStage");
    const labelToggleEnvelope = document.getElementById("labelToggleEnvelope");
    let isEnvelopeOpen = false;

    function toggleHeroEnvelope() {
      isEnvelopeOpen = !isEnvelopeOpen;

      if (isEnvelopeOpen) {
        envelopeStage.classList.add("is-opened");
        if (labelToggleEnvelope) labelToggleEnvelope.textContent = "طي البطاقة";
      } else {
        envelopeStage.classList.remove("is-opened");
        if (labelToggleEnvelope) labelToggleEnvelope.textContent = "فتح البطاقة";
      }
    }

    // Keyboard accessibility for wax seal
    const waxSealButton = document.getElementById("waxSealButton");
    if (waxSealButton) {
      waxSealButton.addEventListener("keydown", function(e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          toggleHeroEnvelope();
        }
      });
    }

    // Smooth scroll helper
    function smoothScrollTo(event, targetSelector) {
      event.preventDefault();
      const targetElement = document.querySelector(targetSelector);
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
      }
    }

    /* ----------------------------------------------------
       4. DELICATE FALLING ROSE PETALS CANVAS
       ---------------------------------------------------- */
    const canvas = document.getElementById("petalsCanvas");
    const ctx = canvas.getContext("2d");
    let petals = [];
    const PETAL_COUNT = 16;

    function resizePetalsCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener("resize", resizePetalsCanvas);
    resizePetalsCanvas();

    class PetalParticle {
      constructor() {
        this.reset(true);
      }

      reset(initial = false) {
        this.x = Math.random() * canvas.width;
        this.y = initial ? Math.random() * canvas.height : -20;
        this.size = Math.random() * 7 + 5;
        this.speedY = Math.random() * 0.7 + 0.3;
        this.speedX = (Math.random() - 0.5) * 0.6;
        this.rotation = Math.random() * 360;
        this.rotationSpeed = (Math.random() - 0.5) * 1.5;
        this.opacity = Math.random() * 0.22 + 0.08;

        const isBurgundy = Math.random() > 0.45;
        this.color = isBurgundy
          ? `rgba(142, 43, 60, ${this.opacity})`
          : `rgba(197, 160, 89, ${this.opacity})`;
      }

      update() {
        this.y += this.speedY;
        this.x += Math.sin(this.y * 0.008) * 0.6;
        this.rotation += this.rotationSpeed;

        if (this.y > canvas.height + 20 || this.x < -20 || this.x > canvas.width + 20) {
          this.reset(false);
        }
      }

      draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate((this.rotation * Math.PI) / 180);
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.ellipse(0, 0, this.size * 0.5, this.size, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }
    }

    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!prefersReducedMotion) {
      for (let i = 0; i < PETAL_COUNT; i++) {
        petals.push(new PetalParticle());
      }

      function loopPetals() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        petals.forEach((p) => {
          p.update();
          p.draw();
        });
        requestAnimationFrame(loopPetals);
      }
      loopPetals();
    }
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

with open('message.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Successfully wrote updated index.html and message.html with 4-flap closed envelope and VIP father name!")

