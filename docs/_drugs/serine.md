---
layout: default
title: Serine
parent: 僅模型預測 (L5)
nav_order: 808
evidence_level: L5
indication_count: 8
monitor_inn: "SERINE"
predicted_indications: ["familial visceral myopathy", "intestinal obstruction", "unclassified intestinal pseudoobstruction", "myopathic intestinal pseudoobstruction", "neuronal intestinal dysplasia, type B", "intestinal pseudoobstruction, neuronal, chronic idiopathic, X-linked", "exercise-induced malignant hyperthermia", "aqueous misdirection"]
last_modified_at: 2026-10-23
description: "Serine：預測新適應症為家族性內臟肌病變（證據等級 L5）。原適應症：知識圖譜記錄：開角型青光眼、肺結核"
---

# Serine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Serine：從青光眼與肺結核到家族性內臟肌病變
{: .text-alpha }

## 一句話總結

Serine（絲胺酸）是一種胺基酸，知識圖譜中記錄的相關用途為開角型青光眼與肺結核（此為知識圖譜關聯，並非核准適應症）。
TxGNN 模型預測它可能對**家族性內臟肌病變 (Familial Visceral Myopathy)** 有效，
但目前**沒有任何臨床試驗或直接相關文獻**支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄：開角型青光眼、肺結核（香港許可證資料未載明核准適應症） |
| 預測新適應症 | 家族性內臟肌病變 |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 核准許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Serine 是蛋白質組成的胺基酸，在香港多以靜脈營養輸液（胺基酸注射液及全靜脈營養乳劑）的成分形式上市。

家族性內臟肌病變是腸道平滑肌的遺傳性疾病（例如 ACTG2 基因變異）。Serine 對這類疾病的平滑肌收縮功能沒有已知的治療作用，也沒有機轉證據顯示它適用。0.9999 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據，缺乏臨床或文獻佐證，因此不應視為療效證據。

其他排名較高的預測（腸阻塞、慢性假性腸阻塞、神經元腸道發育不良、惡性高熱、房水迷流等）同樣沒有試驗或機轉支持。其中「房水迷流」可能與原有的青光眼關聯有關，但並沒有任何機轉可說明 Serine 能處理這個問題。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對預測的新適應症（家族性內臟肌病變），目前無相關文獻。

另有 17 篇文獻是針對相近的「腸阻塞」所檢索，但內容多為關鍵字誤配，例如：
- Peutz-Jeghers 症候群（STK11 絲胺酸/蘇胺酸激酶）
- 旋毛蟲絲胺酸蛋白酶
- PAR2 與大腸炎動物模型
- 黏連蛋白病變（cohesinopathies）

這些研究談的是名稱含「serine」的蛋白質，而非以 L-serine 作為治療藥物，因此不列入證據表，也不支持本預測。

## 香港上市資訊

下列為已登記的主要許可證（以含 Serine 的單一成分登記資料為準，清單可能不完整）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58387 | AMINOLEBAN 8% AMINO ACID INJ | 未載明 | 未載明 |
| HK-46283 | AMINOLEBAN INJ | 未載明 | 未載明 |
| HK-67075 | AMINOVEN INFANT SOLUTION FOR INFUSION 10% W/V | 未載明 | 未載明 |
| HK-36470 | VAMINOLACT I.V. SOLUTION | 未載明 | 未載明 |
| HK-32746 | AMINOPLASMAL HEPA-10% INJ | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：癲癇、焦慮症、精神病類疾患、腎臟病（含慢性腎衰竭、末期腎衰竭）、糖尿病及酮酸中毒、高血鈣、腎結石、心臟病與心血管疾病、維生素 B12 缺乏、巨母細胞性貧血、地高辛中毒、心室顫動等。這些僅是圖譜關聯，實際禁忌請以原廠仿單為準。

其餘警語、禁忌與藥物交互作用資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何針對家族性內臟肌病變的臨床試驗或文獻，也找不到合理的機轉連結，證據等級為 L5。
- 缺乏作用機轉與仿單安全性資料，無法進入安全性篩選。

**若要推進需要：**
- 取得 DrugBank 作用機轉資料，並評估 Serine 與腸道平滑肌病變的機轉關聯
- 下載並解析香港衛生署仿單，補齊警語、禁忌與核准適應症
- 針對家族性內臟肌病變進行系統性文獻檢索，確認是否有 L-serine 的直接研究
- 評估給藥途徑與劑型是否適合（目前上市產品多為靜脈營養輸液）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

