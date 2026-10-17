---
layout: default
title: Allantoin
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Allantoin：預測新適應症為嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)（證據等級 L5）。原適應症：乾癬、類乾癬、脂漏性皮膚炎、單純糠疹、皮膚炎、脂漏性角化症"
monitor_inn: "ALLANTOIN"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "acne keloid", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "hydroa vacciniforme, familial"]
---

# Allantoin
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

# Allantoin：從乾癬與脂漏性皮膚炎到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Allantoin（尿囊素）是外用皮膚製劑常見的成分，原本用於乾癬、脂漏性皮膚炎、皮膚炎等皮膚疾病。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乾癬、類乾癬、脂漏性皮膚炎、單純糠疹、皮膚炎、脂漏性角化症（取自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.56% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Allantoin 是外用的角質溶解、促進傷口癒合及抗刺激成分，其在皮膚疾病中的使用已相當普遍，但與視網膜微血管疾病之間並無已確立的關聯。

TxGNN 的高分來自知識圖譜中的關聯推論。若要說有任何可能的連結（例如抗發炎作用），也都屬於推測。此外，Allantoin 主要為外用劑型，與視網膜這類眼內標的的給藥方式並不相符。

資料中另有數個排名較後的預測，例如痤瘡性瘢痕瘤 (acne keloid)，因 Allantoin 常用於瘢痕與皮膚軟化產品，在生物學上有間接的合理性，可作為較值得優先探索的研究問題。但目前同樣沒有任何實證支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效許可證，皆為單一成分製劑，無已取消者。以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-46597 | CEPTICURA CREAM | 乳膏（依品名） | 未提供 |
| HK-64998 | SCARTUBEX GEL | 凝膠（依品名） | 未提供 |
| HK-60072 | CONTRAX GEL | 凝膠（依品名） | 未提供 |
| HK-19685 | CONTRACTUBEX OINT | 軟膏（依品名） | 未提供 |
| HK-33438 | BELANTOIN CREAM | 乳膏（依品名） | 未提供 |

此外尚有多張眼藥水許可證（如 V-ROHTO EYE DROPS 等），皆為含 Allantoin 的單方製劑。

---

## 安全性考量

- **知識圖譜中的禁忌疾病關聯**（來源為圖譜關聯，非仿單內容）：遺傳性紫質症、紫質代謝疾病、紫質症、腎臟疾病、輸尿管積膿、血液疾病、肝臟疾病、膽囊疾病、G6PD 缺乏症、肝醣儲積症、胱胺酸尿症、半乳糖血症、毛囊炎、脂漏性皮膚炎、皮膚炎。

值得注意的是，圖譜中的禁忌關聯包含脂漏性皮膚炎與皮膚炎，與其原適應症重疊，此類關聯的臨床意義需對照仿單確認。

藥物交互作用查詢未找到相關資料。其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自圖譜模型，沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- 外用製劑與視網膜標的在給藥途徑上不相容，機轉上也缺乏合理連結。

**若要推進需要：**
- 補齊 Allantoin 的作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌資料
- 針對 Allantoin 與糖尿病視網膜病變進行系統性文獻檢索，確認是否有任何前臨床證據
- 評估給藥途徑的可行性（外用製劑不適用於視網膜）
- 優先考慮改為探索與皮膚較相關的預測（如痤瘡性瘢痕瘤），先做外用於瘢痕的文獻回顧
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

