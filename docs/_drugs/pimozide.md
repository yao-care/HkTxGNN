---
layout: default
title: Pimozide
parent: 中證據等級 (L3-L4)
nav_order: 586
evidence_level: L3
indication_count: 5
---

# Pimozide
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Pimozide：從思覺失調症／妥瑞氏症到拔毛癖 (Trichotillomania)

## 一句話總結

Pimozide 是強效 D2 多巴胺受體拮抗劑抗精神病藥，臨床文獻脈絡顯示其長期用於思覺失調症、妥瑞氏症等疾患，但目前未在香港上市。TxGNN 模型預測它可能對**拔毛癖 (Trichotillomania)** 有效，目前有 **10 篇文獻**支持這個方向，尚無專門登記的臨床試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無官方記錄（DrugBank、香港藥證均未載明；文獻脈絡顯示長期用於思覺失調症、妥瑞氏症） |
| 預測新適應症 | 拔毛癖 (Trichotillomania) |
| TxGNN 預測分數 | 99.996%（排名第 172） |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉（MOA）資料——DrugBank 查詢與香港藥證資料皆未記載。根據文獻脈絡，pimozide 屬 diphenylbutylpiperidine 類抗精神病藥，為強效 D2 多巴胺受體拮抗劑，主要臨床應用見於思覺失調症與妥瑞氏症之治療。

Pimozide 的 D2 阻斷作用可調節與強迫／衝動控制相關的紋狀體多巴胺迴路。皮膚科與精神科文獻長期將低劑量 pimozide 作為 SSRI-refractory 拔毛癖的 augmentation（輔助）選項使用，其中一篇開放性世代研究（PMID 1532960）直接觀察到此類病人在加用低劑量 pimozide 後症狀改善。

不過，這些機轉關聯多屬臨床觀察與推論，而非針對拔毛癖設計的對照試驗直接驗證，因此證據強度仍有限。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1532960](https://pubmed.ncbi.nlm.nih.gov/1532960/) | 1992 | Cohort（開放性 augmentation 系列） | J Clin Psychiatry | 低劑量 pimozide 加用於 SSRI 治療的拔毛癖病人，症狀有改善 |
| [15554735](https://pubmed.ncbi.nlm.nih.gov/15554735/) | 2004 | Review | Am J Clin Dermatol | Pimozide 於皮膚科實務之全面回顧，含拔毛癖等心身性皮膚疾患用途 |
| [36802832](https://pubmed.ncbi.nlm.nih.gov/36802832/) | 2023 | Evidence Mapping/Review | J Cutan Med Surg | 原發性心身性皮膚疾患藥物治療之 RCT 證據圖譜 |
| [30446201](https://pubmed.ncbi.nlm.nih.gov/30446201/) | 2018 | Review | Clin Dermatol | 抗精神病藥於皮膚科應用之機轉與臨床角色回顧 |
| [27320510](https://pubmed.ncbi.nlm.nih.gov/27320510/) | 2016 | Review | Tijdschr Psychiatr | 兒童拔毛癖治療選項回顧，指出藥物治療研究投入有限 |
| [11475941](https://pubmed.ncbi.nlm.nih.gov/11475941/) | 2001 | Review | CNS Drugs | 心因性皮膚搔抓症之臨床特徵與治療方法回顧 |
| [10497682](https://pubmed.ncbi.nlm.nih.gov/10497682/) | 1999 | Review | Ann Acad Med Singap | 拔毛癖此一常被低估診斷之精神疾病回顧 |
| [28225970](https://pubmed.ncbi.nlm.nih.gov/28225970/) | 2017 | Case Report | An Bras Dermatol | 拔毛癖病例報告，與圓禿之皮膚鏡鑑別診斷 |
| [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) | 1999 | Case Series（不同藥物） | J Child Adolesc Psychopharmacol | SSRI 難治性拔毛癖加用 risperidone（非 pimozide）之三例報告 |
| [10900563](https://pubmed.ncbi.nlm.nih.gov/10900563/) | 2000 | Case Series（不同疾病） | Int J Psychiatry Med | 妄想性寄生蟲病臨床特徵，非直接針對拔毛癖 |

---

## 其他預測適應症總覽

Evidence Pack 中另列出 4 個 TxGNN 預測適應症，證據強度與建議階段各異，供後續研究優先順序參考：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 | 備註 |
|------|-----------|-----------|---------|---------|------|------|
| 2 | 躁症 (Manic bipolar affective disorder) | 99.993% | L4 | S0 | Hold | 1970-80 年代舊研究顯示抗躁效果，但已被副作用更少的新一代抗精神病藥取代，且 pimozide 有 QT 延長風險 |
| 3 | 失眠 (Insomnia) | 99.968% | L5 | S0 | Hold | 僅 3 篇 1970 年代思覺失調症觀察報告，未以失眠為療效指標，關聯性弱 |
| 4 | 重度情感性疾患 (Major affective disorder) | 99.960% | L3 | S1 | Research Question | 有 1 個 Phase 2 完成試驗（NCT00374244），但受試族群為 clozapine 部分反應之思覺失調症患者，非原發情感性疾患，適應症匹配度中等 |
| 5 | 注意力不足過動症 (ADHD) | 99.922% | L5 | S0 | Hold | 20 篇文獻多為妥瑞氏症合併 ADHD 之管理，判斷為知識圖譜鄰近節點產生的偽陽性訊號，機轉上 D2 拮抗反而可能惡化 ADHD 症狀 |

---

## 安全性考量

安全性資訊請參考原廠仿單。目前缺乏 TFDA（香港衛生署）仿單警語、禁忌症與藥物交互作用資料。

文獻脈絡中另提及 pimozide 屬已知具 QT 間期延長風險之抗精神病藥物（見排名 2 之躁症適應症證據討論），惟此非正式標籤警語，僅供臨床參考。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
拔毛癖為 TxGNN 最高分預測，且有一篇直接觀察 pimozide augmentation 療效的世代研究及多篇專家綜述支持其在 SSRI-refractory 個案中的輔助角色；但缺乏對照試驗，且無專門登記中的臨床試驗，證據等級僅達 L3。同時，本評估存在一項 **Blocking 級資料缺口**（TFDA 仿單警語/禁忌未取得），依規範無法進入 S1 安全性初評，須優先補齊。

**若要推進需要：**
- 補齊 TFDA（香港衛生署）仿單警語與禁忌症資料（Blocking 缺口，來源：官網下載仿單 PDF 解析）
- 補齊正式作用機轉（MOA）資料（來源：DrugBank API 查詢）
- 評估香港引進/上市可行性（目前為未上市藥物，0 張許可證）
- 若擬推進，應設計前瞻性對照試驗驗證 pimozide augmentation 於拔毛癖之療效與 QT 安全性監測方案
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

