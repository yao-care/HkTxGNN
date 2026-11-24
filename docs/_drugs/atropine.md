---
layout: default
title: Atropine
parent: 中證據等級 (L3-L4)
nav_order: 84
evidence_level: L4
indication_count: 2
last_modified_at: 2026-11-24
description: "Atropine：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L4）。原適應症：香港許可證資料未載明"
monitor_inn: "Atropine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Atropine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

## Atropine：從（原適應症未載明）到偏頭痛
{: .text-alpha }

## 一句話總結

Atropine（阿托品）是一種非選擇性的蕈毒鹼型乙醯膽鹼受體拮抗劑，在香港已有多張單方許可證。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前**沒有臨床試驗**，僅有 **11 篇文獻**，且多為動物或體外研究，部分與 atropine 無直接關聯。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 0.9956 |
| 證據等級 | L4 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Atropine 是非選擇性的蕈毒鹼型乙醯膽鹼受體拮抗劑。前臨床文獻指出，膽鹼系統與偏頭痛的病理有關，包括：

- 腦膜肥大細胞介導的膽鹼調控與神經源性發炎（PMID 36485173）
- 刺激大鼠副交感蝶腭神經節，會造成硬腦膜血漿蛋白外滲（PMID 9344563）
- 中樞膽鹼系統參與囓齒類動物的抗痛覺作用（PMID 8930196）

此外，慢性陣發性偏頭痛（chronic paroxysmal hemicrania）的自主神經研究（PMID 2943405）顯示，全身性給予 atropine 可明顯減少發作相關的出汗、流淚與鼻分泌。相關抗膽鹼藥 anisodamine 的藥理學文獻也提供間接支持。

這些資料顯示以蕈毒鹼阻斷作為機轉有一定合理性，但都屬動物或體外數據，**不能證明 atropine 對偏頭痛的臨床療效**。TxGNN 的高分是計算預測，並非臨床證據。根據美國 FDA 核准的 Atropine 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Atropine 在平滑肌、心肌、分泌腺細胞，以及周邊自主神經節和中樞神經系統的蕈毒鹼型膽鹼受體上，競爭性阻斷乙醯膽鹼的作用，包括有機磷中毒所致過量乙醯膽鹼的作用。」英文原文："Atropine competitively blocks the effects of acetylcholine, including excess acetylcholine due to organophosphorus poisoning, at muscarinic cholinergic receptors on smooth muscle, cardiac muscle, secretory gland cells, and in peripheral autonomic ganglia and the central nervous system."（[DailyMed: Atropen Auto-Injector (atropine) prescribing information, Meridian Medical Technologies LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e2d4307d-da8f-49f5-aac0-02355dd9ffb7)，版本日期 2022-09-15；查閱日期 2026-11-19）。

另一個預測適應症「伴腦幹先兆的偏頭痛」目前僅有 1 篇小鼠研究（PMID 31945385），而且該研究顯示膽鹼活化會抑制皮質擴散性抑制（CSD）。這個方向與蕈毒鹼拮抗劑的作用相反，可能反而不利於 atropine，因此證據更弱（L5）。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下列出與 atropine 或偏頭痛機轉較相關的文獻（其餘 4 篇為與 atropine 無關的個案、不良反應或其他藥物研究，不列入）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Anisodamine 是 atropine 衍生物，為非特異性膽鹼拮抗劑，效力與毒性低於 atropine |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | 臨床觀察 | Cephalalgia | 4 名慢性陣發性偏頭痛患者，全身性 atropine 明顯減少發作相關出汗、流淚與鼻分泌 |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | 前臨床機轉研究 | Eur J Neurosci | 大鼠偏頭痛模型中，腦膜肥大細胞介導的膽鹼調控參與神經源性發炎 |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | 動物研究 | Exp Neurol | 刺激大鼠副交感蝶腭神經節可誘發硬腦膜血漿蛋白外滲 |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | 動物研究 | J Pharmacol Exp Ther | 中樞膽鹼系統參與 sumatriptan 在囓齒類的抗痛覺作用 |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | 體外藥理 | Br J Pharmacol | 豚鼠基底動脈尼古丁誘發舒張的機轉研究，atropine 僅作為實驗背景用藥 |

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-47097 | ATROPINE SULPHATE INJ 0.6MG/ML | 單一成分 | ATLANTIC PHARMACEUTICAL LIMITED | 有效 |
| HK-65398 | ATROPINE SULFATE SOLUTION FOR INJECTION 600MCG/ML | 單一成分 | THE INTERNATIONAL MEDICAL COMPANY LIMITED | 有效 |
| HK-66757 | ATROPINE SULFATE COOPER EYE DROPS 1% W/V | 單一成分 | SB PHARMA LIMITED | 有效 |
| HK-08619 | ATROPINE SULPHATE EYE DROPS 1% 'MINIMS' | 單一成分 | BAUSCH & LOMB (HK) LTD | 有效 |
| HK-68445 | ATROJEAN EYE DROPS 0.01% W/V | 單一成分 | JEAN-MARIE PHARMACAL CO LTD | 有效 |

上表列出其中 5 張（共 12 張）。

<!-- licenses:end -->

另有其他許可證（含注射劑與 DHAMOTIL、DIAMOTIL、CELIDIN、SYNCOMIL 等 atropine 與 diphenoxylate 的複方錠劑），張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。

<!-- review:begin hk-lic-20261124b-atropine-1 -->

> **查核更正（2026-11-24）**：原文為「另有 7 張單方許可證（含注射劑與 DHAMOTIL、DIAMOTIL、CELIDIN、SYNCOMIL 等錠劑品項），共計 12 張有效許可證，無已註銷者。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證包括單一成分與複方製劑；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-atropine-1 -->

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分主要項目。
  - 中度：Botulinum toxin type A、Fentanyl、Chlorpheniramine、Acebutolol、Codeine、Tramadol、Dihydrocodeine、Alfentanil、Amitriptyline、Amantadine、Hyoscyamine、Loperamide、Aclidinium、Galantamine、Acetylcholine、Ethanol
  - 輕微：Acetaminophen、Hydrochlorothiazide

  這些多與其他抗膽鹼藥、中樞抑制劑或鴉片類藥物併用時的加成效應有關。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛適應症僅有前臨床與間接機轉證據（L4），沒有任何臨床試驗，TxGNN 高分僅是計算預測。
- 伴腦幹先兆的偏頭痛證據更弱（L5），且唯一的文獻方向可能與 atropine 的作用相反。

**若要推進需要：**
- 補齊 atropine 在香港許可證的核准適應症與劑型資料，以及原廠仿單的警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 進行系統性文獻回顧，確認 atropine 或其他蕈毒鹼拮抗劑在偏頭痛的人體數據
- 評估給藥途徑與劑量的可行性（全身性抗膽鹼副作用，如口乾、心搏過速、尿滯留、青光眼風險）
- 若前述評估支持，再設計小規模探索性臨床試驗

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Atropen Auto-Injector (atropine) prescribing information, Meridian Medical Technologies LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e2d4307d-da8f-49f5-aac0-02355dd9ffb7) |
| 2026-11-24 | 「另有 7 張單方許可證（含注射劑與 DHAMOTIL、DIAMOTIL、CELI」→「另有其他許可證（含注射劑與 DHAMOTIL、DIAMOTI」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

