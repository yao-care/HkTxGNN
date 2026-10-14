---
layout: default
title: Atazanavir
parent: 中證據等級 (L3-L4)
nav_order: 77
evidence_level: L4
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **6** 個
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

# Atazanavir：從 HIV 感染到猿猴免疫缺陷病毒感染

## 一句話總結

Atazanavir 是一種 HIV 蛋白酶抑制劑，原本用於治療 HIV 感染與愛滋病。
TxGNN 模型預測它可能對**猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇**間接的動物模型文獻，且該疾病屬動物模型/獸醫範疇，並非人類藥物再利用的實際目標。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、愛滋病（香港許可證未載明適應症文字） |
| 預測新適應症 | 猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Atazanavir 屬於 HIV-1 蛋白酶抑制劑，其在 HIV 感染中的療效已被證實。SIV 是 HIV-1 在非人類靈長類的對應病毒，兩者同屬慢病毒，蛋白酶結構相近，因此機轉上具備生物學合理性。

不過，這個高分主要反映的是新適應症與既有 HIV 適應症在知識圖譜中的高度相似，而非獨立的新療效訊號。SIV 感染是動物模型或獸醫情境的疾病，沒有人類臨床用途，因此不構成真正的人類新適應症。

其他預測結果中，「貓後天免疫缺乏症候群」同樣缺乏證據；「先天性 HIV」與「愛滋病相關症候群」本質上是現有 HIV 適應症的延伸；「家族性複合型高脂血症（已廢棄術語）」可能反映的是脂質相關副作用關聯，而非療效；「神經發育障礙（伴共濟失調步態等）」則看不出合理的機轉連結，可能是知識圖譜的假象。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | 動物研究 | The Journal of Infectious Diseases | SIV 感染獼猴接受 HAART 後，中樞神經系統病毒複製與發炎減少，但病毒 DNA 仍持續存在；此為複方治療的間接證據，未單獨評估 atazanavir |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68750 | ATAZANAVIR CAPSULES 300MG | 未載明 | 未載明 |
| HK-68749 | ATAZANAVIR CAPSULES 200MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單原文）：肝衰竭、肝病、膽囊疾病、高血糖、糖尿病、糖尿病酮酸中毒、慢性 B 型/C 型肝炎病毒感染、血友病、高膽紅素血症（含遺傳性）、Gilbert 症候群、腎結石、急性尿酸腎病變、房室傳導阻滯、乳酸中毒。
- **藥物交互作用**：共查得 100 筆，以下為部分重要項目：
  - 重大 (Major)：Famotidine、Ranitidine、Rabeprazole、Omeprazole（抑酸劑，可能降低 atazanavir 吸收）、Loperamide、Triamcinolone、Budesonide
  - 中度 (Moderate)：Acarbose、Metformin、Pioglitazone、Alogliptin、Albiglutide、Hydrocortisone、Betamethasone、Aprepitant、Alosetron、Aluminum hydroxide、Calcium carbonate 等

完整的警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的新適應症 SIV 感染屬動物模型疾病，證據僅有 1 篇間接的獼猴複方治療研究，未能單獨評估 atazanavir，且無任何臨床試驗；高分主要源自與既有 HIV 適應症的相似性。
- 在人類相關的預測中，「先天性 HIV」（L3，有觀察性研究）本質上是現有適應症的延伸，現有文獻聚焦於孕期暴露與嬰兒安全性，並非新生兒療效證據，可作為後續研究問題，但不屬於新適應症。

**若要推進需要：**
- 確認是否有人類臨床意義的目標（例如孕期或周產期 HIV 使用情境），而非動物模型疾病
- 取得 atazanavir 的作用機轉資料（MOA）
- 取得香港原廠仿單的警語、禁忌症與核准適應症
- 針對孕期與新生兒族群，整理 atazanavir 的藥動學與安全性證據（如 PMID 24992294 及 PHACS SMARTT 研究）
- 評估與抑酸劑等常用藥物的交互作用管理方案
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

