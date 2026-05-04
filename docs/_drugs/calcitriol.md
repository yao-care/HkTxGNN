---
layout: default
title: Calcitriol
parent: 高證據等級 (L1-L2)
nav_order: 126
evidence_level: L2
indication_count: 7
---

# Calcitriol
{: .fs-9 }

證據等級: **L2** | 預測適應症: **7** 個
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

# Calcitriol：從鈣磷代謝調節到遺傳性低磷血症佝僂病

## 一句話總結

Calcitriol（1,25-dihydroxyvitamin D₃）是維生素 D 的活性終末代謝物，廣泛用於低鈣血症、甲狀旁腺功能低下症及腎性骨病等鈣磷代謝異常的治療。TxGNN 模型共給出 7 項預測適應症；其中**遺傳性低磷血症佝僂病（Hereditary Hypophosphatemic Rickets）**具最充足的臨床證據，目前有 **7 個臨床試驗**和 **20 篇文獻**支持，建議 Proceed with Guardrails。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 低鈣血症、甲狀旁腺功能低下症、腎性骨病（原始資料無登錄，依已知臨床用途補充） |
| 預測新適應症 | 遺傳性低磷血症佝僂病（Hereditary Hypophosphatemic Rickets） |
| TxGNN 預測分數 | 99.28%（7 項預測中最高臨床可行性） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

> **說明**：TxGNN 最高分預測為「obsolete vitamin D deficiency」（99.96%），但該術語已被現代疾病分類取代，導致相關搜尋策略無法捕獲現有臨床證據，屬系統性術語偏誤而非真實證據空白。遺傳性低磷血症佝僂病雖分數略低，卻有最充足的實際臨床依據，故以此為主要評估對象。

---

## 為什麼這個預測合理？

Calcitriol 是體內最具生物活性的維生素 D 形式，由腎臟近端小管 CYP27B1（1α-羥化酶）將 25(OH)D 活化而成。其主要藥理作用為直接與細胞核內的維生素 D 受體（VDR）結合，進而調控腸道鈣磷吸收、骨礦化，以及抑制繼發性 PTH 分泌亢進（詳細 MOA 資料未列入本 Evidence Pack，以已知臨床藥理補充）。

遺傳性低磷血症佝僂病——以 X 連鎖低磷血症（XLH，PHEX 基因突變）最為常見——核心病理為 FGF23 過度分泌。FGF23 一方面抑制腎小管磷再吸收造成低磷血症，另一方面同時壓制 CYP27B1 活性，使 calcitriol 合成量不足以支撐正常骨礦化，形成「雙重打擊」的骨軟化/佝僂病。外源性補充 calcitriol 可完全繞過這個 CYP27B1 受抑制的瓶頸，直接恢復腸道磷（及鈣）吸收，修復骨礦化缺陷，此即 calcitriol 在此疾病中作為數十年標準療法的藥理基礎（PMID: [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/)、[6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/)）。

值得注意的是，近年靶向 FGF23 上游的 burosumab 逐步改變 XLH 治療格局，calcitriol 的定位已部分轉移至 burosumab 不可及地區的替代選擇，或作為輔助療法。這不影響 calcitriol 在此適應症的藥理合理性，但在制定再利用策略時需考量市場定位差異。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | 進行中（未招募） | 20 | **核心直接試驗**：Calcitriol 單一療法（不含磷酸鹽補充）治療 XLH 成人及兒童，評估礦物離子、生長及骨骼礦化結局，劑量遞增設計 |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | 狀態未知 | 100 | 比較高劑量vs低劑量活性維生素 D（calcitriol 或類似物）合併磷酸鹽治療 XLH 兒童療效，探討最佳體重導向劑量 |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | 進行中（未招募） | 27 | INZ-701 治療 ENPP1 缺乏症（FGF23 相關礦化異常），評估療效與安全性；需確認是否含 calcitriol 對照組 |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | 已完成 | 260 | 觀察性機轉研究：住院低磷血症患者中 FGF23 不當分泌的病生理，涵蓋遺傳性及後天性佝僂病，提供疾病背景依據 |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | 尚未開始 | 65 | 磷酸鹽糖尿病（含 XLH）患者中以 ³¹P 光譜影像測量 ATP 濃度，探討肌肉代謝影響 |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | 狀態未知 | 150 | 橫斷面研究：腎結石形成者中 FGF23、Klotho 及 Sclerostin 的角色，與 calcitriol 治療相關性較低 |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | 已撤回 | 0 | Cinacalcet 用於家族性低磷血症佝僂病（測試對象非 calcitriol；已撤回，不計入有效試驗） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | *Lancet* | XLH 完整綜述：PHEX 突變 → FGF23 過度分泌 → calcitriol 合成受抑，確立 calcitriol + 磷酸鹽為傳統標準療法 |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Review | *Calcified Tissue Int* | XLH 診斷與治療最新指引，含 calcitriol 與 burosumab 的定位比較 |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Review | *J Bone Miner Res* | 低磷血症佝僂病與生長遲緩的臨床評估與現代處置策略 |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | *Horm Res Paediatr* | 佝僂病歷史演進與各型治療全面回顧，確認 calcitriol 在礦化缺陷中的核心角色 |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Study | *J Clin Invest* | 高劑量 calcitriol（68 ng/kg/day）治療 XLH 5 例，成功修復傳統療法無效的骨軟化症 |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical Study | *N Engl J Med* | 11 名維生素 D 抵抗型佝僂病兒童接受 calcitriol 治療，增加腸道磷吸收，改善骨骼 X 光表現 |
| [17117305](https://pubmed.ncbi.nlm.nih.gov/17117305/) | 2006 | Review | *Arq Bras Endocrinol Metab* | 各型低磷血症骨軟化症的病生理機轉，calcitriol 作為修復 1α-羥化活性不足的藥理依據 |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Cohort | *Pediatr Endocrinol Rev* | 127 例 XLH 患者早期 calcitriol + 磷酸鹽治療對自然病程及生長速率的影響 |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Clinical Study | *Calcified Tissue Int* | 17 名兒童接受 calcitriol + 磷酸鹽治療，6 個月後中軸及四肢骨礦物密度均有改善 |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | *Nutrients* | 各類佝僂病的維生素 D 及類似物（含 calcitriol、alfacalcidol）治療適應症分析 |

---

## 香港上市資訊

本次 Evidence Pack 顯示 Calcitriol 在香港**無登記許可證**（登記數：0）。安全性及適應症資訊請直接查閱原廠仿單或香港衛生署藥物辦公室資料庫。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：Calcitriol 因治療窗窄，臨床上需特別監測**高鈣血症**（噁心、嗜睡、多尿）、**高鈣尿症**及**腎鈣化**等特有毒性，建議定期追蹤血鈣、尿鈣及腎功能。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Calcitriol 用於遺傳性低磷血症佝僂病（尤其 X 連鎖低磷血症）已有數十年的療效文獻基礎，機轉連結明確（繞過 FGF23 抑制的 CYP27B1 缺陷），並有直接針對 calcitriol 的臨床試驗（NCT03748966、NCT03820518）進行中，整體達 L2 證據等級。惟 burosumab 等新興療法的出現改變了治療格局，且 calcitriol 在香港目前無許可登記，需評估進入策略。

**若要推進需要：**
- 確認 Calcitriol 在香港的實際上市/進口許可狀態（本次資料顯示「未上市」，需向衛生署藥物辦公室核實）
- 取得完整仿單以進行安全性初評（DG001），尤其高鈣血症及腎鈣化的監測計畫
- 補充作用機轉資料（DG002），完善機轉關聯性分析文件
- 確認 NCT03820518 試驗的完成狀態及已發表結果
- 就 calcitriol 與 burosumab 的臨床定位（替代/輔助/低資源地區一線）進行情境分析，明確再利用策略的目標族群
- 對其他高評分預測（腎小管性酸中毒 L4、副甲狀腺功能低下症 L5）進行補充文獻搜尋，以現代術語更新搜尋策略
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

