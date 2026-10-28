---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 538
evidence_level: L5
indication_count: 3
monitor_inn: "LOPINAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-28
description: "Lopinavir：預測新適應症為猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)（證據等級 L5）。原適應症：知識圖譜中記錄的 HIV 感染、愛滋病"
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Lopinavir：從 HIV 感染到猴免疫缺陷病毒感染
{: .text-alpha }

## 一句話總結

Lopinavir 是 HIV 蛋白酶抑制劑，知識圖譜中記錄的原適應症為 HIV 感染與愛滋病。
TxGNN 模型預測它可能對**猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效。
目前**無臨床試驗**，僅有 **3 篇**前臨床動物研究文獻，且這些研究是在多藥合併療法中使用 lopinavir，屬間接支持，並非人類新適應症的證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的 HIV 感染、愛滋病（香港許可證資料中未載明核准適應症文字） |
| 預測新適應症 | 猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 核准許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，lopinavir 是 HIV 蛋白酶抑制劑，通常與 ritonavir 合併使用，其對 HIV 的療效是此預測的基礎。

SIV 是與 HIV 親緣相近的慢病毒，其蛋白酶與 HIV-1 蛋白酶結構相似，而 HIV-1 蛋白酶正是 lopinavir 的已知標靶，因此機轉上的類推有一定合理性。

不過，SIV 感染是非人類靈長類的疾病模型，並非人類臨床適應症。現有文獻多屬獼猴研究，且 lopinavir 是合併療法的一部分，只能間接支持其原本的 HIV 用途，不能視為針對此疾病的直接證據。因此依規則，證據等級定為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | 前臨床動物研究 | Journal of Virology | 4 隻感染 SIVmac251 的食蟹猴接受 7 天四藥抗病毒治療，觀察病毒快速下降的動態 |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | 前臨床動物研究 | Microbes and Infection | 建構帶有 HIV-1 蛋白酶基因的 SHIV-pr，可感染恆河猴，作為蛋白酶抑制劑體內療效試驗的工具 |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | 前臨床動物研究 | Journal of Virological Methods | 2 隻慢性感染 SHIV 89.6P 的恆河猴口服 AZT、3TC 與 lopinavir/ritonavir 28 天，評估對 CD8 亞群的影響 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68129 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG | 未提供 | 未提供 |
| HK-65831 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG | 未提供 | 未提供 |
| HK-55200 | KALETRA TAB | 未提供 | 未提供 |
| HK-66676 | LOPINAVIR AND RITONAVIR TABLETS USP 100MG/25MG | 未提供 | 未提供 |
| HK-66612 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG | 未提供 | 未提供 |

（另有 1 張許可證 HK-48165，品名為 KALETRA ORAL SOL，由 AbbVie 持有，此處依規定最多列 5 張。）

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單內容）：長 QT 症候群、尖端扭轉型心室頻脈、胰臟炎、肝病、肝硬化、慢性 B 型與 C 型肝炎、高血糖、糖尿病及酮酸中毒、高三酸甘油脂血症、高膽紅素血症、心臟傳導疾病、房室傳導阻滯、心肌病變、冠狀動脈疾病、血友病等。
- **藥物交互作用**：共查得 65 筆，以下為部分範例：
  - 重度：Dolasetron、Papaverine（皆可能與心律相關風險有關，需審慎評估）
  - 中度：Acarbose、Dapagliflozin、Metformin、Levofloxacin、Ondansetron、Palonosetron、Famotidine 及多種瀉劑
  - 輕度：Cimetidine、Clotrimazole

完整警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的疾病是非人類靈長類的動物模型，不是人類臨床適應症，且僅有間接的前臨床合併療法研究，沒有直接針對此疾病評估 lopinavir 單獨作用的研究。
- 此預測對人類的臨床轉化價值有限，目前不適合推進。

**若要推進需要：**
- 明確此預測的目標用途（如作為 HIV 藥物的動物模型驗證，或其他應用）
- 補充 lopinavir 的詳細作用機轉資料
- 取得香港仿單的核准適應症、警語與禁忌症
- 有針對 lopinavir 單藥在 SIV 模型中的直接研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

