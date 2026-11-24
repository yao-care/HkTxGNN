---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 521
evidence_level: L5
indication_count: 4
monitor_inn: "LETROZOLE"
predicted_indications: ["nipple carcinoma", "Ehrlich tumor carcinoma", "breast fibrocystic disease", "benign mammary dysplasia"]
last_modified_at: 2026-11-24
description: "Letrozole：預測新適應症為乳頭癌 (nipple carcinoma)（證據等級 L5）。香港藥劑製品註冊：13 張（有效 12 張）"
---

# Letrozole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Letrozole: 乳頭癌 (nipple carcinoma)
{: .text-alpha }

## 一句話總結

Letrozole 是一種非類固醇芳香環轉化酶抑制劑，在香港已有多張單方許可證，但目前資料未提供核准適應症文字。
TxGNN 模型預測它可能對**乳頭癌 (Nipple Carcinoma)** 有效，
目前**沒有臨床試驗**，僅有 **8 篇文獻**（多為病例報告）與此方向相關，且無研究直接以 letrozole 治療乳頭癌。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 乳頭癌 (nipple carcinoma) |
| TxGNN 預測分數 | 0.9976 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 13 張） |
| 許可證數 | 13 張（有效 12 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Letrozole 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「部分乳癌的生長受雌激素刺激或維持。對於被認為具荷爾蒙反應性（即雌激素及／或黃體素受體陽性或受體狀態未知）之乳癌，其治療曾包括多種降低雌激素濃度（卵巢切除術、腎上腺切除術、腦下垂體切除術）或抑制雌激素作用（抗雌激素及黃體素類藥物）的方法。[…] Letrozole 是芳香環轉化酶系統的非類固醇競爭性抑制劑；它抑制雄激素轉化為雌激素。」英文原文："The growth of some cancers of the breast is stimulated or maintained by estrogens. Treatment of breast cancer thought to be hormonally responsive (i.e., estrogen and/or progesterone receptor positive or receptor unknown) has included a variety of efforts to decrease estrogen levels (ovariectomy, adrenalectomy, hypophysectomy) or inhibit estrogen effects (antiestrogens and progestational agents). […] Letrozole is a nonsteroidal competitive inhibitor of the aromatase enzyme system; it inhibits the conversion of androgens to estrogens."（[DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406)，版本日期 2026-06-11；查閱日期 2026-11-19）。根據已知資訊，Letrozole 屬於芳香環轉化酶抑制劑，可阻斷雄激素轉化為雌激素，是荷爾蒙受體陽性乳癌的既有治療藥物。

乳頭癌與副乳癌通常源自乳房組織，若為荷爾蒙受體陽性，理論上與雌激素依賴的生物特性相近，因此機轉上有合理性。

但需要留意：現有文獻只有病例報告與病例回顧，沒有針對此疾病的臨床試驗。高預測分數主要反映模型中與乳癌的網絡相近性，並非獨立的臨床驗證。文獻中也沒有一篇直接研究 letrozole 用於乳頭癌，因此證據等級定為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33120755](https://pubmed.ncbi.nlm.nih.gov/33120755/) | 2020 | 回溯性研究／病例報告 | Medicine | 探討新輔助內分泌治療對乳房低分化神經內分泌癌的效果，此疾病罕見、無標準治療 |
| [41607681](https://pubmed.ncbi.nlm.nih.gov/41607681/) | 2026 | 病例報告＋文獻回顧 | Clinical Case Reports | 起源於乳頭的實性乳突原位癌，診斷與治療證據有限 |
| [34495428](https://pubmed.ncbi.nlm.nih.gov/34495428/) | 2021 | 病例報告＋文獻回顧 | Surgical Case Reports | 乳房下皺褶區副乳癌的罕見病例 |
| [40395253](https://pubmed.ncbi.nlm.nih.gov/40395253/) | 2025 | 病例報告 | Cureus | 乳癌伴血性乳頭分泌物，術後出現腋下復發 |
| [39682607](https://pubmed.ncbi.nlm.nih.gov/39682607/) | 2024 | 病例報告 | Diagnostics | 同時發生的轉移性乳房下副乳癌與同側乳癌 |
| [42040393](https://pubmed.ncbi.nlm.nih.gov/42040393/) | 2026 | 病例報告 | Clinical Case Reports | 反極性高細胞乳癌的分子特徵（IDH1 R132 突變），非以治療為主 |
| [42305961](https://pubmed.ncbi.nlm.nih.gov/42305961/) | 2026 | 病例報告 | Frontiers in Medicine | 副乳癌、乳突狀甲狀腺癌與鼻乳突瘤同時發生 |
| [42416948](https://pubmed.ncbi.nlm.nih.gov/42416948/) | 2026 | 病例報告 | Cureus | 旺盛型乳小葉原位癌的超音波影像表現，非以治療為主 |

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-42537 | FEMARA TAB 2.5MG | 單一成分 | NOVARTIS PHARMACEUTICALS (HK) LIMITED | 有效 |
| HK-65626 | LETROZOLE SANDOZ TABLETS 2.5MG | 單一成分 | SANDOZ HONG KONG LIMITED | 有效 |
| HK-64679 | ACCORD LETROZOLE TABLETS 2.5MG | 單一成分 | JACOBSON MARKETING LIMITED | 有效 |
| HK-61004 | LETROZOLE-TEVA TAB 2.5MG | 單一成分 | TEVA PHARMACEUTICAL HONG KONG O/B TEVA PHARMACEUTICAL HONG KONG LIMITE… | 已註銷 |
| HK-62001 | LETROZOLE STADA TABLETS 2.5MG | 單一成分 | HONG KONG MEDICAL SUPPLIES LTD | 有效 |

上表列出其中 5 張（共 13 張）。

<!-- licenses:end -->

目前含本藥成分的許可證皆為單方（HK-61004 已註銷；張數見本頁快速總覽與「香港上市資訊」的許可證表），上表僅列出其中 5 張。

<!-- review:begin hk-lic-20261117-letrozole-1 -->

> **查核更正（2026-11-24）**：原文為「目前共有 12 張有效單方許可證，」。已更正：HK-61004 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。 已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-69106 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-letrozole-1 -->

## 細胞毒性

Letrozole 為荷爾蒙（內分泌）治療藥物，不屬於傳統細胞毒性化療藥物。若用於腫瘤治療，請參考原廠仿單的警語與注意事項。

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（來自 TxGNN 知識圖譜，並非仿單內容）：肝衰竭、肝硬化、骨質疏鬆、停經後骨質疏鬆、高膽紅素血症、遺傳性高膽紅素血症、Gilbert 症候群、腦血管疾病。
- **藥物交互作用**：資料庫共記錄 100 項。其中 Aprepitant 為中度；其餘多數等級未知，例如 Calcitriol、Glimepiride、Lansoprazole、Granisetron、Famotidine、Acetylsalicylic acid、Metformin、Omeprazole。
- 針對良性乳房疾病的預測，雌激素抑制可能帶來骨質流失、血管舒縮症狀與關節痛等風險，需審慎評估。

其他安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻皆為病例報告，且無研究直接評估 letrozole 治療乳頭癌，證據等級僅為 L5。
- 高預測分數主要反映與乳癌的網絡相近性，尚不足以支持推進。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌。
- 補充詳細的作用機轉資料。
- 收集乳頭癌或副乳癌患者的荷爾蒙受體狀態與 letrozole 治療結果的系統性資料（如回溯性世代研究）。
- 規劃針對性的臨床研究，並制定骨質密度與肝功能的安全性監測計畫。

**其他預測適應症（供參考）：**
- Ehrlich 腫瘤癌（分數 0.9975）：僅有小鼠奈米粒子配方研究，無人體證據，證據等級 L5，建議 Hold。
- 乳房纖維囊腫病（0.9962）與良性乳腺發育不良（0.9954）：無臨床試驗與文獻，證據等級 L5，建議 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「目前共有 12 張有效單方許可證，」→「目前含本藥成分的許可證皆為單方（HK-61004 已註銷；張」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

