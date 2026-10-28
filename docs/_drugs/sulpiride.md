---
layout: default
title: Sulpiride
parent: 僅模型預測 (L5)
nav_order: 841
evidence_level: L5
indication_count: 9
monitor_inn: "SULPIRIDE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia X-linked", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "syndromic myopia", "atypical glycine encephalopathy"]
last_modified_at: 2026-10-23
description: "Sulpiride：預測新適應症為視網膜失養症，伴或不伴眼外異常（證據等級 L5）。原適應症：思覺失調症"
---

# Sulpiride
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

## Sulpiride：從思覺失調症到視網膜失養症
{: .text-alpha }

## 一句話總結

Sulpiride 是選擇性多巴胺 D2/D3 受體拮抗劑，知識圖譜記錄its 原本用於思覺失調症。
TxGNN 模型預測它可能對**視網膜失養症（伴或不伴眼外異常）**有效，
目前沒有臨床試驗，僅有 **2 篇**動物實驗文獻，屬間接的機轉性證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 思覺失調症（來自知識圖譜的記錄；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 視網膜失養症，伴或不伴眼外異常 |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 核准許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠 MOA 欄位無內容）。根據藥理資料，Sulpiride 對 D2 與 D3 多巴胺受體具選擇性，對 D4 受體親和力低；另有資料顯示它與碳酸酐酶 1、7、12 有交互作用。

視網膜中的多巴胺 D2 類受體會調節視網膜神經節細胞對光的反應。在視網膜色素病變的 P23H 大鼠模型中，D2 拮抗劑（含 sulpiride）似乎能增加神經節細胞的光敏感度，並把異常的長潛時 ON 型細胞轉為 OFF 型。這是此預測目前唯一的機轉線索。

但這些結果僅屬動物模型的電生理觀察，並未顯示 sulpiride 能減緩光感受器退化或改善遺傳性視網膜失養症患者的視力，效果方向（有益或有害）也不明確。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26717015](https://pubmed.ncbi.nlm.nih.gov/26717015/) | 2015 | 前臨床（動物電生理） | PLoS One | 探討 D2 類受體拮抗劑對野生型與 P23H 大鼠視網膜神經節細胞光反應的影響 |
| [27788033](https://pubmed.ncbi.nlm.nih.gov/27788033/) | 2016 | 前臨床（動物電生理） | J Ocul Pharmacol Ther | 在 P23H 視網膜色素病變大鼠中，sulpiride 等 D2 拮抗劑似可改善神經節細胞的視覺反應；另測試 haloperidol 與 clozapine 的作用 |

這兩篇研究以視網膜色素病變動物模型為對象，並非直接針對預測的疾病（遺傳性視網膜失養症）在人體或疾病本身的研究，因此證據等級仍定為 L5。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65024 | GAMOTIL CAPSULES 50MG | 未載明 | 未載明 |
| HK-53702 | VICK-SULPIRIDE CAP 50MG | 未載明 | 未載明 |
| HK-40717 | SULPIREN TAB 50MG | 未載明 | 未載明 |
| HK-52650 | SUPIDE CAP 50MG | 未載明 | 未載明 |
| HK-44716 | SULIDE CAP 50MG | 未載明 | 未載明 |

另有 HK-53700（VICK-SULPIRIDE TAB 200MG）。本報告所列 6 張許可證皆為單一成分製劑且有效，但許可證資料中沒有核准適應症文字。

## 安全性考量

- **藥物交互作用／藥理標的**：本次資料僅列出藥理標的，未列出藥物間的交互作用，包括 D2 受體、D3 受體，以及碳酸酐酶 1、7、12。

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗，僅有 2 篇間接的動物電生理研究，且效果方向不明，證據等級為 L5。
- 排名其餘的預測（如水腦無腦症、腓骨肌萎縮症、近視等）同樣缺乏支持證據，部分在機轉上甚至不利，不建議推進。

**若要推進需要：**
- 在遺傳性視網膜失養症模型中驗證 sulpiride 對光感受器存活與視功能的影響（含效果方向）。
- 取得香港仿單的警語、禁忌症與核准適應症資料，並補齊 MOA 資料。
- 評估全身性使用 D2 拮抗劑用於眼科疾病的風險效益，以及是否需要局部給藥途徑。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

