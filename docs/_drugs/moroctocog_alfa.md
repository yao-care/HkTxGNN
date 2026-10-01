---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 589
evidence_level: L5
indication_count: 5
---

# Moroctocog Alfa
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

# Moroctocog Alfa：從 A 型血友病（推定）到血小板釋放障礙

> 註：Evidence Pack 缺少原適應症資料（`original_indications` 為空）。Moroctocog alfa 為 B 區域刪除之重組第八凝血因子，臨床上用於 A 型血友病，此處為依藥物類別的推定，並非來自輸入資料。

## 一句話總結

Moroctocog alfa（商品名 XYNTHA）是 B 區域刪除的重組第八凝血因子（FVIII），一般用於補充 A 型血友病缺乏的凝血因子。
TxGNN 模型預測它可能對**血小板釋放障礙 (Primary Release Disorder of Platelets)** 有效，但**沒有任何直接支持的臨床試驗或文獻**，機轉上也缺乏合理性，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏（許可證未載明核准適應症） |
| 預測新適應症 | 血小板釋放障礙 (Primary Release Disorder of Platelets) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Moroctocog alfa 是重組 FVIII，作用是補充血漿中缺少的凝血因子。

血小板釋放障礙是血小板顆粒分泌功能本身的缺陷，問題出在血小板，不在 FVIII。補充 FVIII 對這個缺陷沒有直接的機轉依據。

TxGNN 分數很高（99.97%），較可能來自知識圖譜中凝血／出血疾病的共同鄰近關係，而非真正的功能關聯。因此這個預測應視為待驗證的假說，不宜當作有力的證據。

其他預測（僅有模型分數，皆為 L4–L5）：

| 預測適應症 | TxGNN 分數 | 證據等級 | 機轉評估 |
|-----------|-----------|---------|---------|
| 偽性血管性血友病 (Pseudo-von Willebrand disease) | 99.97% | L5 | 病因為 GPIbα 功能增強突變，補充 FVIII 無法矯正；無試驗與文獻 |
| Glanzmann 血小板無力症 | 99.96% | L5 | 病因為 GPIIb/IIIa 缺乏；標準處置是輸血小板或重組 FVIIa，補充 FVIII 無明確依據 |
| 後天性凝血因子缺乏 | 99.88% | L4 | 有生物學關聯（後天性 A 型血友病），但抑制物會中和人類序列 FVIII；標準處置是旁路藥物或豬序列 FVIII |
| Scott 症候群 | 99.86% | L5 | 病因為血小板磷脂絲胺酸暴露缺陷（TMEM16F），補充 FVIII 無法矯正；無試驗與文獻 |

## 臨床試驗證據

以下為首要預測（血小板釋放障礙）的試驗。7 個登記試驗經評估均與本藥及此適應症無關（相關性 C 級）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | 招募中 | 200 | COVID-19 疫苗接種後症候群的檢驗與症狀評估，與本藥無關 |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | 尚未招募 | 80 | 急性骨髓性白血病誘導化療的凝血指標觀察，無關 |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | 完成 | 30 | PEG 化 rFVIII（BAX 855）用於重度 A 型血友病手術，產品與疾病皆不同 |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | 招募中 | 25 | 人工肝支持系統用於慢加急性肝衰竭，無關 |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | 完成 | 159 | rFVIIIFc-VWF-XTEN（BIVV001）用於 12 歲以上重度 A 型血友病，產品不同 |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | 完成 | 74 | BIVV001 用於 12 歲以下兒童 A 型血友病，產品不同 |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | 招募中 | 45 | 經頸靜脈肝內門體分流術患者的止血探索，無關 |

次要預測「後天性凝血因子缺乏」有較多間接相關的試驗（最相關者如下，均為不同產品，非 moroctocog alfa）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A | 招募中 | 3000 | ATHN 出血性疾病治療的自然史世代研究 |
| [NCT06550882](https://clinicaltrials.gov/study/NCT06550882) | N/A | 招募中 | 9 | 韓國 OBIZUR（豬序列 FVIII）用於後天性 A 型血友病的上市後監測 |
| [NCT04580407](https://clinicaltrials.gov/study/NCT04580407) | Phase 2/3 | 完成 | 5 | 重組豬 FVIII（TAK-672）用於日本後天性 A 型血友病，樣本極小 |
| [NCT02610127](https://clinicaltrials.gov/study/NCT02610127) | N/A | 完成 | 53 | OBIZUR 用於後天性 A 型血友病的上市後安全性評估 |
| [NCT01178294](https://clinicaltrials.gov/study/NCT01178294) | Phase 2/3 | 完成 | 29 | 重組豬 FVIII（OBI-1）用於後天性 A 型血友病出血 |

## 文獻證據

首要預測（血小板釋放障礙）目前無相關文獻。

以下為其他預測適應症的文獻，皆為間接證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25525118](https://pubmed.ncbi.nlm.nih.gov/25525118/) | 2015 | 世代研究 | Blood | 後天性 A 型血友病（GTH-AH 01/2010）緩解與存活的預後因子，102 位患者 |
| [25765796](https://pubmed.ncbi.nlm.nih.gov/25765796/) | 2015 | Review | Rinsho Ketsueki | 後天性凝血因子抑制物的綜述，多數為抗 FVIII 自體抗體 |
| [26517066](https://pubmed.ncbi.nlm.nih.gov/26517066/) | 2015 | Case report | Blood Coagul Fibrinolysis | 後天性 FVIII 抑制物與後續非何杰金氏淋巴瘤的個案與文獻回顧 |
| [14161416](https://pubmed.ncbi.nlm.nih.gov/14161416/) | 1964 | Review | Blood | 後天性血液凝固異常的臨床意義 |
| [14179492](https://pubmed.ncbi.nlm.nih.gov/14179492/) | 1964 | Case series | Br J Haematol | 3 例血小板無力症研究（Glanzmann） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66835 | XYNTHA 注射用粉劑及溶劑 250IU | 注射劑（粉劑及溶劑） | 資料未載明 |
| HK-66834 | XYNTHA 注射用粉劑及溶劑 1000IU | 注射劑（粉劑及溶劑） | 資料未載明 |
| HK-66836 | XYNTHA 注射用粉劑及溶劑 500IU | 注射劑（粉劑及溶劑） | 資料未載明 |

三張許可證皆由 PFIZER CORPORATION HONG KONG LIMITED 持有。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 高 TxGNN 分數缺乏實質支持：首要預測沒有相關試驗或文獻，機轉上補充 FVIII 也無法矯正血小板功能缺陷。
- 五項預測中，僅「後天性凝血因子缺乏」有間接的生物學關聯，但人類序列 FVIII 會被抑制物中和，標準處置是旁路藥物或豬序列 FVIII。

**若要推進需要：**
- 補齊藥物原適應症與作用機轉資料（DrugBank）。
- 取得香港衛生署仿單，確認警語與禁忌症。
- 若要探索，優先評估「後天性凝血因子缺乏」，先做文獻與機轉的系統性回顧，確認抑制物存在下人類序列 FVIII 是否有任何角色。
- 血小板釋放障礙、偽性血管性血友病、Glanzmann 血小板無力症與 Scott 症候群建議暫不推進，除非出現新的機轉證據。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

