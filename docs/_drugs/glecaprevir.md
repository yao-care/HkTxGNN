---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 5
---

# Glecaprevir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Glecaprevir：從慢性 C 型肝炎到 HIV 感染症

## 一句話總結

Glecaprevir 是泛基因型直接作用抗病毒藥（DAA），以 NS3/4A 蛋白酶抑制劑機轉用於慢性 C 型肝炎治療（通常與 pibrentasvir 合用）。
TxGNN 模型預測它可能對 **HIV 感染症 (HIV Infectious Disease)** 有效，預測分數高達 **99.87%**。
然而，此次檢索到的 **15 項臨床試驗**與 **20 篇文獻**均為 HCV 研究，無任何一項直接以 HIV 病毒量為治療終點，機轉上亦缺乏直接支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎（由文獻推導；JSON 欄位為空） |
| 預測新適應症 | HIV 感染症 (HIV Infectious Disease) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

### 藥物機轉

目前 Evidence Pack 中缺乏正式 MOA 欄位資料，但根據已知文獻（PMID 30090878、31537106），Glecaprevir 是 **HCV NS3/4A 絲胺酸蛋白酶抑制劑**，可阻斷 HCV 多蛋白前體的切割加工，進而抑制 HCV 複製。其作用靶點高度專一於 HCV 病毒蛋白，對哺乳類宿主蛋白酶影響極低。

### 預測的表面關聯性

HCV 感染與 HIV 感染在流行病學上高度重疊：歐美 HIV 感染者中約 25–30% 合併 HCV 共感染（PMID 29595065）。正因如此，大量 Glecaprevir 的 Phase 3 臨床試驗（如 EXPEDITION-2、ENDURANCE 系列）均納入 HIV/HCV 共感染患者作為次群，使知識圖譜中 Glecaprevir 節點與 HIV 疾病節點之間形成大量關聯邊。

### 為何預測不具機轉合理性

**HIV 與 HCV 的複製機制根本不同**：HIV 為反轉錄病毒，依賴逆轉錄酶（RT）、整合酶（IN）及 HIV 蛋白酶（PR）；HIV 蛋白酶雖同屬蛋白酶，但屬**天冬胺酸蛋白酶（aspartyl protease）**，與 HCV NS3/4A 絲胺酸蛋白酶無結構同源性。Glecaprevir 對 HIV 逆轉錄酶、整合酶及 HIV 蛋白酶均無已知抑制活性。TxGNN 高分（0.9987）的最可能原因，是模型將「曾廣泛出現於 HIV/HCV 共感染族群的研究」誤解為「可治療 HIV」，屬知識圖譜共感染節點驅動的系統性誤預測，**並非真實藥理訊號**。

---

## 臨床試驗證據

以下為與 HIV 感染相關性最高的試驗（所有試驗終點均為 **HCV SVR12**，HIV 僅為共感染分層因子，非治療靶點）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | 完成 | 153 | EXPEDITION-2：G/P 在 HCV GT1–6 合併 HIV-1 共感染患者的療效與安全性；主要終點為 HCV SVR12，非 HIV 病毒量 |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | 完成 | 546 | G/P 對亞洲非肝硬化慢性 HCV 患者（含 HIV 共感染次群）的雙盲 RCT；HIV 狀態為分層因子 |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | 完成 | 160 | G/P 對亞洲代償性肝硬化 HCV 患者（含 HIV 共感染）的開放標籤研究；HCV SVR12 為主要終點 |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | 完成 | 87 | HCV 根除後 HIV/HCV 共感染者心血管風險追蹤；HCV 治療後 CV 生物標記變化為主要研究方向 |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | 完成 | 45 | 急性 HCV 感染（含/不含 HIV 共感染）接受 4 週 G/P 治療的療效評估 |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) | Phase 3 | 完成 | 33 | MAGELLAN-3：G/P + SOF + RBV 用於 AbbVie 研究中 HCV 病毒學失敗患者；多為 HIV/HCV 共感染 |
| [NCT04352309](https://clinicaltrials.gov/study/NCT04352309) | N/A | 完成 | 99 | 俄羅斯真實世界 G/P 8 週治療肝硬化 HCV 患者；HIV 共感染為次群分析 |
| [NCT04189627](https://clinicaltrials.gov/study/NCT04189627) | N/A | 完成 | 99 | 俄羅斯青少年（12–18 歲）慢性 HCV 真實世界研究；含 HIV/HCV 共感染次群 |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | N/A | 完成 | 17 | 遠距醫療提供 HCV 治療、PrEP 及 MOUD 給針具交換場所高風險族群；HIV 預防服務同時提供 |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | 尚未招募 | 30 | G/P 於妊娠期 HCV 感染（含 HIV 共感染）的 PK 與安全性研究；預計 2026 年開始 |

> ⚠️ **重要提示**：上述 10 項試驗的治療標的均為 **HCV**，HIV 感染狀態僅作為納入分層或安全性監測條件，無任何一項試驗以 HIV RNA 抑制率或 CD4 計數為主要終點。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Systematic Review / Meta-analysis | Int J Antimicrob Agents | 13 項研究共 3,082 患者，G/P 整體 SVR12 率 97.8%；無直接 HIV 治療數據 |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Real-world Cohort | J Antimicrob Chemother | HIV/HCV 共感染真實世界 G/P 療效，SVR 率高；研究終點為 HCV 清除，非 HIV 病毒量 |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | DDI 研究 | J Infect Dis | G/P 與 HIV 抗反轉錄病毒藥物交互作用研究；確認部分 ART 藥物與 G/P 合用時需調整劑量 |
| [32754824](https://pubmed.ncbi.nlm.nih.gov/32754824/) | 2020 | Real-world Cohort | Adv Ther | 代償性肝硬化 HCV 初治患者 8 週 G/P 真實世界療效確認 |
| [39829106](https://pubmed.ncbi.nlm.nih.gov/39829106/) | 2025 | Real-world Cohort | Kaohsiung J Med Sci | 台灣 HCV 登錄研究（TACR），CKD 患者接受 G/P 8 週療效 |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | Review | Hepatology Int | G/P 擴大治療覆蓋、縮短療程並降低成本的綜述；含 HIV 共感染族群說明 |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiology | G/P 藥理、療效、安全性綜述；含 HIV/HCV 共感染次章節 |
| [31537106](https://pubmed.ncbi.nlm.nih.gov/31537106/) | 2020 | Review | Ann Pharmacother | G/P 首個 8 週泛基因型療程藥學綜述（含 ≥12 歲族群） |
| [36415300](https://pubmed.ncbi.nlm.nih.gov/36415300/) | 2022 | Case Report | J Prev Med Hyg | 義大利首例：HIV 感染者合用 G/P 與 ART 期間出現間接高膽紅素血症與黃疸 |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | HCV 蛋白酶抑制劑綜述，說明 HIV/HCV 共感染盛行率（歐美約 25–30%）與 DAA 在此族群的應用 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **附加注意事項（來自文獻 PMID 31504702）**：Glecaprevir 與部分 HIV 抗反轉錄病毒藥物（如 atazanavir、darunavir 增效劑）存在顯著藥物交互作用（透過 CYP3A4/P-gp/OATP 路徑），若未來評估 HIV/HCV 共感染患者使用情境，需系統性評估 ART 合用方案的藥物交互作用。

---

## 結論與下一步

**決策：Hold**

**理由：**
Glecaprevir 靶向 HCV NS3/4A **絲胺酸蛋白酶**，HIV 則依賴逆轉錄酶、整合酶及 **天冬胺酸蛋白酶**複製，兩者無結構同源性，Glecaprevir 對 HIV 複製酶系無已知抑制活性。TxGNN 分數（99.87%）高度可疑，最可能源於大量 HIV/HCV 共感染 Phase 3 試驗在知識圖譜中形成的密集節點連結，屬模型系統性誤預測而非真實藥理訊號。

此外，**其餘 4 項預測適應症（HBV 感染症、SIV 感染症、貓免疫缺陷症候群、HEV 感染症）亦均為 Hold（L5 證據）**：HBV 採用 cccDNA/DNA 聚合酶機轉無 NS3/4A 同源靶點；SIV 與 FIV 為動物病原體且機轉相同（知識圖譜「免疫缺陷疾病節點」批次誤預測）；HEV ORF1 蛋白酶雖與 NS3/4A 同屬絲胺酸蛋白酶超家族而具理論假說，但目前無任何體外活性數據或 HEV 文獻支持。

**若要推進 HEV 假說需要：**
- 完成體外 Glecaprevir 對 HEV ORF1 蛋白酶的 IC₅₀ 測定（細胞培養或重組蛋白系統）
- 確認 Glecaprevir 的詳細 MOA 文件（從 DrugBank API 取得）
- HEV 感染相關文獻搜尋（目前搜尋結果為零）

**若要推進任何 HIV 方向則需要：**
- 確認 HIV 蛋白酶（天冬胺酸蛋白酶）對 Glecaprevir 的結構對接模擬結果
- 基於現有機轉理解，此方向**不建議推進**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

