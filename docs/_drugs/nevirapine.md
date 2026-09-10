---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 521
evidence_level: L5
indication_count: 3
---

# Nevirapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Nevirapine：從 HIV-1 感染到猴免疫缺乏病毒 (SIV) 感染

## 一句話總結

Nevirapine 是一種非核苷類反轉錄酶抑制劑（NNRTI），公開資訊顯示原本用於 HIV-1 感染治療；但本次證據包對藥物基本資料（原適應症、MOA）標記為 **Data Gap**，且該藥目前**未在香港上市**。TxGNN 模型針對此藥給出三個高分預測（分數均 ≈99.8%），其中證據最完整的是**猴免疫缺乏病毒感染 (SIV infection)**，有 **17 篇文獻**支持，但均為體外/動物模式的機轉研究，**無任何臨床試驗**；另兩個預測（貓愛滋病、罕見神經發育疾病）幾乎無實證支持，其中神經發育疾病一項已被判定為知識圖譜雜訊。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（藥物公開已知用途；本證據包未提供詳細來源資料，列為 Data Gap） |
| 預測新適應症 | 猴免疫缺乏病毒感染 (Simian Immunodeficiency Virus infection) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L4（僅有前臨床/機轉相關研究，無臨床試驗） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

> 註：TxGNN 同時給出另兩個高分預測——貓愛滋病 (feline acquired immunodeficiency syndrome, 分數 99.85%) 與一項罕見神經發育疾病 (分數 99.82%)。前者無任何臨床試驗或文獻證據；後者證據包內已明確標註「零試驗、零文獻，應視為模型雜訊，不建議投入驗證資源」，故本報告不將其列為主要分析對象。

---

## 為什麼這個預測合理？

Nevirapine 屬於 NNRTI 類藥物，其藥理作用是直接結合並抑制反轉錄酶的活性位點——這個酶是所有慢病毒（lentivirus）複製週期中的關鍵蛋白，HIV-1、HIV-2、SIV 皆共享類似的反轉錄酶結構與功能。

文獻證據顯示，學界長期使用「SIV/SHIV 嵌合病毒模型」（將 SIV 的反轉錄酶基因置換為 HIV-1 反轉錄酶）來研究 NNRTI 類藥物（包含 nevirapine）的抗病毒活性與抗藥性演化，因為野生型 SIV 本身對 NNRTI 不敏感，必須透過基因置換才能測試。這說明 TxGNN 抓到的關聯，本質上反映的是「NNRTI 機轉」與「反轉錄酶結構相似的慢病毒」之間的藥理連結，而非 SIV 本身是一個獨立可治療的人類適應症。

需要特別指出：SIV 感染是靈長類動物模式疾病，並非人類臨床適應症；貓愛滋病同樣是貓科動物疾病。這兩個預測對藥物再利用的**臨床開發價值有限**，較適合理解為「驗證 nevirapine 機轉延伸性」的研究工具，而非可推進人體臨床試驗的新適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | 動物模式研究 | Journal of Virology | 建立表現 HIV-1 反轉錄酶的 SIV/HIV 嵌合病毒，用於在豬尾獼猴中研究 NNRTI 抗藥性演化 |
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | 體外機轉研究 | Biochem Biophys Res Commun | RT-SHIV 嵌合病毒對 NNRTI 類藥物高度敏感，證實 HIV-1 反轉錄酶置換後可被 NNRTI 抑制 |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | 動物模式研究 | Virology | 表現 HIV-1 反轉錄酶的 RT-SHIV 在恆河猴陰道感染模式中可穩定複製，用於 NNRTI 相關研究 |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | 動物模式研究 | AIDS Res Hum Retroviruses | 食蟹猴 RT-SHIV 感染模式用於觀察 NNRTI 治療下抗藥性的產生與逆轉 |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | 體外機轉研究 | Virology | NNRTI 類藥物可抑制 HIV-1 與 SIV 病毒顆粒的內源性反轉錄，探討其作為殺病毒劑的潛力 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | 體外機轉研究 | Antiviral Therapy | 評估 16 種已核准抗 HIV 藥物（含 NNRTI 類）對 HIV-2、SIV、SHIV 之抗病毒活性，供治療與暴露後預防參考 |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | 體外機轉研究 | Antimicrob Agents Chemother | 明確測試 nevirapine 與其他藥物合併使用於 HIV-1/SIV 病毒株之抑制效果 |
| [27748043](https://pubmed.ncbi.nlm.nih.gov/27748043/) | 2017 | 體外機轉研究 | Chem Biol Drug Des | 新型小分子對 HIV-1 具專一性，對 SIV、貓免疫缺乏病毒（FIV）等其他反轉錄病毒無效，凸顯病毒株間反轉錄酶差異 |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | 體外機轉研究 | Antivir Chem Chemother | 氟喹諾酮衍生物對多株 HIV-1、HIV-2 及 SIV 具廣效抗病毒活性 |
| [1283296](https://pubmed.ncbi.nlm.nih.gov/1283296/) | 1992 | 體外機轉研究 | Antimicrob Agents Chemother | FTC 對 HIV-1、HIV-2、SIV、FIV 均具選擇性抑制作用，機轉與去氧胞苷代謝路徑相關 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

*（本證據包標記主要警語、禁忌症、藥物交互作用查詢皆為 Data Gap 或查無資料，無法於此報告呈現具體內容。）*

---

## 結論與下一步

**決策：Hold**

**理由：**
- 三個 TxGNN 高分預測中，證據最完整的「SIV 感染」仍僅止於體外與動物模式的機轉研究（L4），無任何人體臨床試驗；且 SIV/貓愛滋病本質上是動物疾病，非人類臨床適應症，臨床開發路徑不明確。
- 另一項「罕見神經發育疾病」預測已被評為知識圖譜雜訊（零試驗、零文獻、機轉上無合理連結），不建議投入資源。

**若要推進需要：**
- 補齊藥物基本資料 Data Gap（原適應症全文、MOA、香港仿單警語與禁忌症），此為 Blocking 等級缺口，需先解決才能進入安全性初評（S1）。
- 若要重新評估「SIV 感染」此方向，需釐清其實際臨床對應族群（例如是否轉化為其他人類反轉錄病毒相關適應症）而非直接以動物模式疾病作為終點。
- 確認 nevirapine 在香港的上市／引進計畫，目前無許可證，市場可行性待評估。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

