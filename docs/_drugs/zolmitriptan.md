---
layout: default
title: Zolmitriptan
parent: 中證據等級 (L3-L4)
nav_order: 944
evidence_level: L4
indication_count: 3
---

# Zolmitriptan
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Zolmitriptan：從急性偏頭痛到腦幹先兆偏頭痛

## 一句話總結

Zolmitriptan 是 5-HT1B/1D 受體促效劑（triptan 類），文獻顯示其用於偏頭痛急性期治療。
TxGNN 模型預測它可能對**腦幹先兆偏頭痛 (Migraine with Brainstem Aura)** 有效，但目前**沒有臨床試驗**，只有 **18 篇間接文獻**，且沒有一篇直接在此亞型測試 zolmitriptan。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性偏頭痛（依文獻判斷；香港許可證未提供適應症文字） |
| 預測新適應症 | 腦幹先兆偏頭痛 (Migraine with Brainstem Aura) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前缺資料。不過文獻摘要指出，zolmitriptan 是選擇性 5-HT1B/1D 受體促效劑，臨床前研究顯示它能同時抑制中樞與周邊的三叉神經血管活化。大型隨機對照試驗顯示，它對一般偏頭痛的 2 小時緩解率與無痛率良好。

腦幹先兆偏頭痛屬於偏頭痛亞型，所以從機轉上看，模型預測有生物學上的合理性。

但這不是乾淨的老藥新用機會，原因有三：
- 現有文獻談的是一般偏頭痛、兒童偏頭痛、其他 triptan（frovatriptan、eletriptan）和臨床前藥理，沒有針對腦幹先兆的 zolmitriptan 研究。
- 此藥本來就用於偏頭痛，新適應症與原適應症高度重疊，新增價值有限。
- triptan 類仿單通常把偏癱型或基底型偏頭痛列為禁忌或警示，原因是理論上有血管收縮疑慮。這一點需對照香港現行仿單確認。

另外兩個預測（萎縮性蚓狀皮膚病 atrophoderma vermiculata、眉部毛囊性紅斑 ulerythema ophryogenesis）預測分數都很高（99.90%、99.83%）。但兩者都找不到機轉關聯、沒有任何試驗或文獻，證據等級皆為 L5，很可能是知識圖譜的假象，不建議推進。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27329280](https://pubmed.ncbi.nlm.nih.gov/27329280/) | 2016 | RCT | Headache | TEENZ 試驗（NCT01211145）：評估 zolmitriptan 鼻噴劑用於 12–17 歲青少年偏頭痛急性治療，主要終點為 2 小時無痛率（偏頭痛一般族群，非腦幹先兆） |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT 次族群分析 | Neurol Sci | frovatriptan 與 zolmitriptan 2.5 mg 用於有先兆偏頭痛的比較，僅 18 位受試者（一般先兆，非腦幹先兆） |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | 隨機研究 | Cephalalgia | 36 位早期異常性疼痛的偏頭痛患者隨機分入六種 triptan 組，比較疼痛減輕程度 |
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | 臨床報告 | Headache | 報告 triptan 用於基底型偏頭痛與長時間先兆偏頭痛的經驗（最接近目標適應症，但摘要未載明具體藥物與結果） |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | 指引／證據評估 | Headache | 美國頭痛學會對成人偏頭痛急性治療藥物的證據評估 |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | 統合分析 | J Headache Pain | frovatriptan 與 rizatriptan、zolmitriptan、almotriptan 在有先兆偏頭痛的療效比較 |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opin Pharmacother | zolmitriptan 為 5-HT1B/1D 促效劑，隨機對照試驗顯示 2 小時反應率與無痛率良好 |
| [10473025](https://pubmed.ncbi.nlm.nih.gov/10473025/) | 1999 | Review | Drugs | 2.5 mg 與 5 mg 口服起效快，45 分鐘即可見明顯緩解，多數反應者療效可維持 |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | 臨床前藥理 | Cephalalgia | 兼具 5HT1B/1D 部分促效作用，可抑制中樞與周邊三叉神經血管活化 |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Front Neurol | 前庭型偏頭痛現有治療選項回顧（相關亞型，非腦幹先兆） |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62233 | PMS-ZOLMITRIPTAN TABLETS 2.5MG | TRENTON-BOMA LTD |
| HK-43324 | ZOMIG TAB 2.5MG | DKSH HONG KONG LIMITED |

兩張許可證在資料中都沒有劑型與核准適應症文字。

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢未找到資料。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高，但沒有任何臨床試驗，也沒有針對腦幹先兆的 zolmitriptan 研究，證據只到 L4。
- triptan 類對此亞型可能有禁忌或警示，在安全性釐清前不宜推進。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認警語與禁忌症，特別是基底型與偏癱型偏頭痛。此項是目前的阻擋性資料缺口。
- 補齊 DrugBank 的作用機轉資料。
- 搜尋並評估 zolmitriptan 或其他 triptan 在腦幹先兆偏頭痛的直接證據，包括病例報告與安全性資料。
- 評估此預測相對於現有偏頭痛適應症的實際新增價值。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

