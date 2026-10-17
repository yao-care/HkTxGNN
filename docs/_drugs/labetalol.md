---
layout: default
title: Labetalol
parent: 僅模型預測 (L5)
nav_order: 500
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Labetalol：預測新適應症為惡性高血壓腎病變 (Malignant Hypertensive Renal Disease)（證據等級 L5）。原適應症：高血壓 (Hypertension)"
monitor_inn: "Labetalol"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Labetalol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Labetalol：從高血壓到惡性高血壓腎病變

## 一句話總結

Labetalol 是兼具 α1 與非選擇性 β 腎上腺素受體阻斷作用的降血壓藥，原本用於高血壓及高血壓急症。
TxGNN 模型預測它可能對**惡性高血壓腎病變 (Malignant Hypertensive Renal Disease)** 有效，
但目前**沒有臨床試驗**，也**沒有直接支持此適應症的文獻**，證據僅來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓 (Hypertension) |
| 預測新適應症 | 惡性高血壓腎病變 (Malignant Hypertensive Renal Disease) |
| TxGNN 預測分數 | 99.08% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理知識，Labetalol 同時阻斷 α1 與 β 受體，可降低全身血管阻力並控制血壓，已用於高血壓及高血壓急症。

惡性高血壓腎病變是嚴重高血壓造成的標靶器官（腎臟）併發症。因此，它與原適應症的關聯主要來自「控制血壓」這個共同環節，兩者在疾病譜上相近。

不過要注意，這比較像是原適應症的延伸，而不是全新的藥物再利用機會。0.99 的預測分數只是模型輸出，沒有任何試驗或文獻佐證，機轉推論也只是依據一般藥理學。

**其他預測適應症的簡要評估：**

- **惡性腎血管性高血壓**（分數 99.08%）：降壓機轉上合理，但唯一連結的文獻（PMID 7242419，1981 年，藥物誘發血管炎的個案報告）僅描述 Labetalol 與 minoxidil 用於初期血壓控制，並非針對腎血管性高血壓的研究，無直接臨床支持。
- **肺部疾病／缺氧所致肺高壓**與**機轉不明的多因性肺高壓**（分數皆約 99.08%）：缺乏可信的機轉連結。Labetalol 作用於體循環阻力與心率，非選擇性 β 阻斷可能誘發支氣管痙攣、削弱心輸出儲備，也可能使右心功能惡化。高分很可能反映「高血壓」字詞的相似性，而非肺血管生物學。這兩項應視為安全性疑慮，而非治療訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測適應症（惡性高血壓腎病變），目前無相關文獻。

以下為其他預測適應症所連結的文獻（皆未直接證實 Labetalol 的療效）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | 個案報告 | Med J Aust | 惡性高血壓個案，初期以 minoxidil 與 labetalol 控制血壓；用於腎血管性高血壓預測，但並非針對此疾病的研究 |
| [8487154](https://pubmed.ncbi.nlm.nih.gov/8487154/) | 1993 | 臨床比較研究 | J Perinat Med | 20 位子癇前症孕婦比較 labetalol 與 hydralazine 對新生兒適應的影響（非肺高壓） |
| [24384582](https://pubmed.ncbi.nlm.nih.gov/24384582/) | 2014 | Review | Eur J Anaesthesiol | 子癇前症的病理生理與處置策略 |
| [10862260](https://pubmed.ncbi.nlm.nih.gov/10862260/) | 2000 | Review | Presse Med | β 阻斷劑中毒，labetalol 屬較具毒性的藥物之一 |
| [1735870](https://pubmed.ncbi.nlm.nih.gov/1735870/) | 1992 | Review | J Post Anesth Nurs | 高血壓患者的術後急性高血壓 |
| [7658039](https://pubmed.ncbi.nlm.nih.gov/7658039/) | 1995 | Review | J Indian Med Assoc | 子癇 |
| [10566616](https://pubmed.ncbi.nlm.nih.gov/10566616/) | 1999 | 前臨床 | Oncol Res | 比較血管擴張藥（含 labetalol）對小鼠腫瘤 pH 的影響 |
| [19380903](https://pubmed.ncbi.nlm.nih.gov/19380903/) | 2009 | 動物研究 | Reprod Sci | 綿羊模型中 labetalol 或 pindolol 對胎盤與胎兒血流動力學的影響 |
| [23020995](https://pubmed.ncbi.nlm.nih.gov/23020995/) | 2013 | 動物研究 | Eur J Obstet Gynecol Reprod Biol | 綿羊模型中 labetalol 或 pindolol 對胎兒心臟功能的影響 |
| [26380574](https://pubmed.ncbi.nlm.nih.gov/26380574/) | 2015 | 個案系列 | J Pediatr Pharmacol Ther | 小兒陣發性交感神經過度活躍，以 morphine 處置（非 labetalol 研究） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-02802 | TRANDATE TAB 100MG | — | 未提供 |
| HK-02800 | TRANDATE TAB 200MG | — | 未提供 |
| HK-57922 | TRANDATE INJ 5MG/ML (TAIWAN) | — | 未提供 |
| HK-68126 | LABETALOL HYDROCHLORIDE SOLUTION FOR INJECTION/INFUSION 25MG/5ML | — | 未提供 |
| HK-68453 | PHARMANIAGA LABETALOL HYDROCHLORIDE SOLUTION FOR INJECTION/INFUSION 25MG/5ML | — | 未提供 |

香港共有 7 張有效許可證，均為單一成分製劑，另有 APT-LABETALOL 錠劑 100 mg 與 200 mg（HK-54799、HK-54798）。劑型與核准適應症文字在本次整理的資料中皆缺漏。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來源為知識圖譜的藥物－疾病關聯，非仿單原文）：包括肝衰竭、肝病、肝性腦病變、腎臟疾病、無尿、胰臟炎、膽囊疾病、糖尿病及糖尿病酮酸中毒、全身性紅斑性狼瘡、痛風、低血壓、房室傳導阻滯、肺氣腫與支氣管疾病、焦慮症等。其中房室傳導阻滯、支氣管疾病與肺氣腫，與非選擇性 β 阻斷的風險相符，也加強了對肺高壓預測的疑慮。
- **藥物交互作用**：共查得 100 筆，以下為部分重點：
  - 嚴重（Major）：Epinephrine、Dolasetron
  - 中度（Moderate）：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide、Morphine、Atropine、Cimetidine、Canagliflozin、Dapagliflozin、Chlorpropamide 等
  - 輕微（Minor）：Acetylsalicylic acid、Magnesium oxide

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 4 個預測適應症均僅有模型預測（L5），沒有任何臨床試驗，也沒有直接支持的文獻。
- 惡性高血壓腎病變與原適應症高度重疊，屬原適應症的延伸；肺高壓相關預測則有 β 阻斷可能造成傷害的疑慮，不建議推進。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA）。
- 取得香港仿單的警語、禁忌與核准適應症內容。
- 針對惡性高血壓腎病變，系統性搜尋 Labetalol 的臨床與觀察性研究，確認是否已屬現行適應症範圍。
- 若要評估肺高壓方向，需先完成安全性審視（支氣管痙攣、右心功能），目前不建議進行。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

