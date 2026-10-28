---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 9
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-28
description: "Glimepiride：預測新適應症為局部僵直肢症候群 (Focal Stiff Limb Syndrome)（證據等級 L5）。原適應症：第二型糖尿病"
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Glimepiride：從第二型糖尿病到局部僵直肢症候群
{: .text-alpha }

## 一句話總結

Glimepiride 是一種磺醯脲類（sulfonylurea）降血糖藥，知識圖譜中記錄其用於第二型糖尿病。
TxGNN 模型預測它可能對**局部僵直肢症候群 (Focal Stiff Limb Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第二型糖尿病（知識圖譜記錄；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 局部僵直肢症候群 (Focal Stiff Limb Syndrome) |
| TxGNN 預測分數 | 0.9975 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 19 張／共 19 張） |
| 許可證數 | 19 張（有效 19 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識而言，Glimepiride 屬磺醯脲類，作用是關閉胰臟 β 細胞的 K-ATP 通道，促進胰島素分泌。

局部僵直肢症候群是一種與 GABA 神經傳導及抗 GAD（麩胺酸脫羧酶）抗體相關的自體免疫或神經性僵硬疾病。可能的間接關聯是此類疾病與糖尿病在自體免疫方面有重疊，這可能是 TxGNN 模型（深度學習）給出高分的原因，反映的是模型從相關疾病間學到的相似性，而非生物學證據。但這個推論只是推測，磺醯脲類並無已知作用於此疾病的神經機轉。

整體而言，0.9975 的高分僅是 TxGNN 模型（深度學習）的運算結果，可能反映模型從相關疾病間學到的相似性，並未獲得任何試驗或文獻佐證，不能視為療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 19 張有效的單一成分許可證，以下列出 5 張主要許可證（核准適應症文字在本次整理的資料中未載明）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42323 | AMARYL TAB 2MG | 錠劑 | 未載明 |
| HK-42325 | AMARYL TAB 4MG | 錠劑 | 未載明 |
| HK-62478 | LIMERAL TABLETS 4MG | 錠劑 | 未載明 |
| HK-62479 | LIMERAL TABLETS 2MG | 錠劑 | 未載明 |
| HK-57874 | GLIMEPIRIDE SANDOZ TAB 4MG | 錠劑 | 未載明 |

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：腎臟疾病、肝臟疾病、膽囊疾病、充血性心衰竭、腦下垂體功能不全（含多種先天性與後天性型態）、低促性腺素性性腺功能低下、卡爾曼氏症候群、希恩症候群、胸腺疾病、骨質疏鬆（含停經後骨質疏鬆）、感染性疾病。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：Phenylephrine、Acebutolol、Acetazolamide、Famotidine、Ranitidine、Acitretin、Formoterol、Pseudoephedrine、Ketorolac、Epinephrine、Ibuprofen、Ethinylestradiol、Hydrocortisone、Albiglutide、Salbutamol、Ethanol、Nitazoxanide、Hydrochlorothiazide
  - 輕微：Hydrocortisone（外用）、Alclometasone（外用）

完整警語與禁忌症請參考原廠仿單。

---

## 其他排名較前的預測（皆為 L5、Hold）

| 預測疾病 | TxGNN 分數 | 備註 |
|---------|-----------|------|
| 典型僵人症候群 | 0.9975 | 與抗 GAD65 自體免疫及第一型糖尿病共病有關，磺醯脲類無已知相關神經機轉 |
| 骨發育不良 (Opsismodysplasia) | 0.9974 | 與 INPPL1 突變及胰島素訊號有概念上的關聯，純屬假設 |
| 硫胺素反應性功能障礙症候群 | 0.9973 | 患者常併發糖尿病，即使有益也僅限血糖控制 |
| 局部性脂肪失養症（多種類型） | 0.9956–0.9962 | 僅為 TxGNN 模型學到的疾病相近性，無藥理依據 |
| 胰臟發育不全 | 0.9955 | 此病缺乏 β 細胞，Glimepiride 作用機轉上不合理；唯一檢索到的文獻（PMID 12720536）為胰島素瘤內視鏡超音波影像研究，與本藥及此疾病治療無關 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，不是生物學證據；沒有任何直接研究該疾病的臨床試驗或文獻，證據等級為 L5。
- 磺醯脲類促進胰島素分泌的機轉與僵直肢症候群的神經免疫病理之間，沒有支持的機轉連結。

**若要推進需要：**
- 補充詳細的作用機轉資料與機轉層面的分析
- 取得香港原廠仿單的警語、禁忌症與核准適應症
- 搜尋是否有 Glimepiride 或磺醯脲類用於僵人症候群譜系疾病的病例報告或前臨床研究
- 在有任何直接證據之前，不建議進入臨床評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

