---
layout: default
title: Colistin
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Colistin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Colistin：從細菌感染到慢性鼻竇炎（及其他預測適應症）

## 一句話總結

Colistin（黏菌素，polymyxin E）是一種多黏菌素類抗生素，用於治療多重抗藥性革蘭氏陰性菌感染。
TxGNN 預測的前 10 名新適應症中，排名第一為**感染後血管炎 (postinfectious vasculitis)**，但該項僅有模型預測、無任何研究支持；
證據相對最具體的是**慢性鼻竇炎 (chronic rhinosinusitis)**，目前有 **1 篇霧化 bacitracin/colimycin 的隨機對照先導研究**（合併用藥）及數篇間接文獻。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證未載明適應症文字；依藥理為革蘭氏陰性菌感染） |
| 預測新適應症 | 感染後血管炎 (postinfectious vasculitis)（排名第 1） |
| TxGNN 預測分數 | 99.91%（排名第 1 的預測） |
| 證據等級 | L5（排名第 1 的預測）；同批預測中最高為 L3（慢性鼻竇炎） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold（排名第 1 的預測）；慢性鼻竇炎為 Research Question |

> 補充：TxGNN 分數極高（皆 >99%）但與實際證據不成正比，排名第 1 的預測很可能只是知識圖譜中與感染相關節點相近所致。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Colistin 是多黏菌素類抗生素，會結合革蘭氏陰性菌外膜的脂多醣 (LPS)，破壞外膜完整性而殺菌。

**感染後血管炎、感染後症候群等：**這類疾病多為免疫複合物介導，並非活動性感染，機轉上沒有明確路徑。
Chagas 心肌病由寄生蟲引起，感染相關溶血性尿毒症候群 (HUS) 由毒素造成內皮損傷，且 Colistin 有腎毒性；感染性尿道狹窄為纖維化後遺症。這些預測都缺乏機轉依據，較可能是知識圖譜的假象。

**慢性鼻竇炎與鼻竇炎：**Colistin 對綠膿桿菌等革蘭氏陰性菌有活性，特別是囊性纖維化 (CF) 或多重抗藥性病例。
霧化或局部給藥可降低全身暴露，機轉上較合理，但目前只有個案與間接證據。

## 臨床試驗證據

以下僅列出與 Colistin 較相關者（各預測適應症的試驗多為活動性抗藥菌感染，屬間接證據）。

**post-bacterial disorder（排名第 2）**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06488794](https://clinicaltrials.gov/study/NCT06488794) | Phase 2/3 | 尚未招募 | 400 | 霧化 colistimethate 預防兒童呼吸器相關肺炎（對照安慰劑） |
| [NCT06440304](https://clinicaltrials.gov/study/NCT06440304) | Phase 4 | 招募中 | 108 | 碳青黴烯抗藥鮑氏不動桿菌感染的治療策略 |
| [NCT01631968](https://clinicaltrials.gov/study/NCT01631968) | N/A | 完成 | 2948 | 含 erythromycin 與 colistin 骨水泥預防膝關節置換術後感染 |
| [NCT01732250](https://clinicaltrials.gov/study/NCT01732250) | Phase 4 | 完成 | 406 | Colistin 單用 vs 合併 meropenem 治療多重抗藥菌感染 |
| [NCT01970371](https://clinicaltrials.gov/study/NCT01970371) | Phase 3 | 完成 | 69 | Plazomicin vs colistin 治療碳青黴烯抗藥腸桿菌感染 |
| [NCT02452047](https://clinicaltrials.gov/study/NCT02452047) | Phase 3 | 完成 | 50 | Imipenem/relebactam vs colistimethate + imipenem 治療抗藥菌感染 |
| [NCT03894046](https://clinicaltrials.gov/study/NCT03894046) | Phase 3 | 完成 | 207 | Sulbactam-durlobactam vs colistin 為基礎方案治療不動桿菌感染 |
| [NCT06198764](https://clinicaltrials.gov/study/NCT06198764) | Phase 3 | 招募中 | 80 | 中國成人碳青黴烯抗藥革蘭氏陰性菌感染，colistimethate 合併 meropenem |
| [NCT06827756](https://clinicaltrials.gov/study/NCT06827756) | Phase 4 | 完成 | 90 | Norfloxacin、nitazoxanide、colistin 用於自發性細菌性腹膜炎二級預防 |
| [NCT05922124](https://clinicaltrials.gov/study/NCT05922124) | Phase 4 | 招募中 | 734 | Cefiderocol + 氨苄西林舒巴坦 vs colistin 為基礎方案治療 CRAB |

**post-infectious syndrome（排名第 3）**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02389036](https://clinicaltrials.gov/study/NCT02389036) | Phase 3 | 完成 | 20010 | ICU 消化道選擇性去污染（含 colistin）預防感染的整群交叉試驗 |
| [NCT06051513](https://clinicaltrials.gov/study/NCT06051513) | N/A | 招募中 | 404 | Colistimethate 治療碳青黴烯抗藥腸桿菌感染 |
| [NCT01023087](https://clinicaltrials.gov/study/NCT01023087) | N/A | 完成 | 70 | Polymyxin E 相關腎功能損害的觀察研究（安全性） |
| [NCT02134106](https://clinicaltrials.gov/study/NCT02134106) | Phase 2/3 | 撤回 | 0 | XDR 革蘭氏陰性菌合併抗生素試驗，未收案，無資料 |

其餘預測適應症（感染後血管炎、Chagas 心肌病、感染相關 HUS、感染性尿道狹窄、副傷寒、鼻竇炎、慢性鼻竇炎、慢性篩竇炎）目前無相關臨床試驗登記。

> 以上試驗皆針對活動性感染的治療或預防，並非「感染後疾病」，與預測適應症僅為關鍵字層級的間接關聯。

## 文獻證據

**慢性鼻竇炎 / 鼻竇炎（證據最具體）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18575008](https://pubmed.ncbi.nlm.nih.gov/18575008/) | 2008 | 雙盲隨機對照交叉先導研究（依標題判斷） | Rhinology | 霧化 bacitracin/colimycin 用於頑固性慢性鼻竇炎（金黃色葡萄球菌），為合併用藥，無法分離 colistin 貢獻 |
| [19308657](https://pubmed.ncbi.nlm.nih.gov/19308657/) | 2009 | 個案報告 | Int J Hematol | 靜脈注射 colistin 成功治療 AML 患者由多重抗藥綠膿桿菌引起的鼻竇炎、眼眶蜂窩性組織炎與肺炎 |
| [25016384](https://pubmed.ncbi.nlm.nih.gov/25016384/) | 2014 | 藥動學研究 | J Antimicrob Chemother | CF 患者經鼻給予 tobramycin 與 colistin 的全身吸收，作為安全性替代指標 |
| [34296343](https://pubmed.ncbi.nlm.nih.gov/34296343/) | 2022 | Review | Eur Arch Otorhinolaryngol | CF 相關慢性鼻竇炎治療選項回顧 |
| [23406585](https://pubmed.ncbi.nlm.nih.gov/23406585/) | 2013 | 世代研究（間接） | Am J Rhinol Allergy | CF 患者鼻竇手術與密集追蹤對致病菌的影響，非 colistin 特異 |
| [27879058](https://pubmed.ncbi.nlm.nih.gov/27879058/) | 2017 | 世代研究（間接） | Int Forum Allergy Rhinol | 鼻竇手術可改善原發性纖毛運動障礙患者生活品質與肺功能 |
| [24315789](https://pubmed.ncbi.nlm.nih.gov/24315789/) | 2014 | 體外／前臨床 | Int J Antimicrob Agents | Colistin 對浮游態綠膿桿菌的殺菌效果不依賴羥自由基生成 |
| [41599109](https://pubmed.ncbi.nlm.nih.gov/41599109/) | 2025 | 體外／前臨床 | Pharmaceutics | Ceragenins 合併 ivacaftor 抑制鼻竇炎致病菌生物膜（非 colistin） |

**副傷寒**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [14126225](https://pubmed.ncbi.nlm.nih.gov/14126225/) | 1964 | 歷史臨床觀察 | Iryo | 傷寒與副傷寒觀察報告，無摘要，標題未顯示 colistin 證據 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63662 | COLISTIN POWDER FOR SOLUTION FOR INJECTION 150MG | 注射用粉劑（依品名） | 未提供 |
| HK-42135 | MULTIBIO SUSPENSION INJ (VET) | 注射懸液（依品名） | 未提供（獸醫用產品） |

## 細胞毒性

Colistin 為抗菌藥物，非抗腫瘤藥物，不適用此章節。

## 安全性考量

安全性資訊請參考原廠仿單。

補充：Evidence Pack 中的觀察研究（NCT01023087）以 polymyxin E 相關腎功能損害為主題，且 Colistin 已知具腎毒性，在感染相關 HUS 等腎損傷情境需特別留意。香港衛生署仿單的警語與禁忌尚未取得，藥物交互作用查詢無結果。

## 結論與下一步

**決策：Hold**（排名第 1 的感染後血管炎，及其餘 L5 預測）
慢性鼻竇炎、鼻竇炎建議列為 **Research Question**，可另行深入評估。

**理由：**
- 前六名預測（感染後血管炎、post-bacterial disorder、post-infectious syndrome、Chagas 心肌病、感染相關 HUS、感染性尿道狹窄）機轉上缺乏依據，多為知識圖譜假象，或試驗僅屬活動性感染的間接證據。
- 慢性鼻竇炎有霧化 colimycin 合併用藥的先導研究，機轉上較合理，但僅屬 L3，且非 colistin 單獨效果。
- 高 TxGNN 分數不代表療效，證據不足。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌、適應症），此為目前阻擋安全性初篩的缺口
- 補齊 MOA 資料（DrugBank）
- 針對慢性鼻竇炎：確認 PMID 18575008 的實際試驗設計與結果，並評估霧化／局部給藥的安全性（腎毒性、神經毒性、氣道刺激）
- 確認局部給藥劑型在香港是否可取得（現有許可證為注射劑）
- 評估與現行標準療法（局部類固醇、其他抗生素）的相對價值，以及 CF 族群的適用性

> 本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

